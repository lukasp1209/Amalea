#!/usr/bin/env python3
"""
🎨 Data Augmentation Explorer - Streamlit App
=====================================

Interactive web app for exploring Data Augmentation techniques
for CIFAR-10 image classification.

Author: IU Data Analytics Course
Date: 2025
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="🎨 Data Augmentation Explorer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff7f0e;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .augmentation-box {
        border: 2px solid #4ecdc4;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f0fdfa;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🎨 Data Augmentation Explorer</h1>', unsafe_allow_html=True)
st.markdown("**Interaktive Exploration von Data Augmentation Techniken für Computer Vision**")

# Sidebar Configuration
st.sidebar.header("🎛️ Augmentation Parameter")

# Load and Cache Data
@st.cache_data
def load_cifar10():
    """Load CIFAR-10 dataset"""
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    
    # Normalize
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # Class names
    classes = [
        'Flugzeug', 'Auto', 'Vogel', 'Katze', 'Hirsch',
        'Hund', 'Frosch', 'Pferd', 'Schiff', 'LKW'
    ]
    
    return x_train, y_train, x_test, y_test, classes

# Load data
x_train, y_train, x_test, y_test, classes = load_cifar10()

# Create Augmentation Pipeline
@st.cache_resource
def create_augmentation_pipeline(
    rotation_range, zoom_range, brightness_range, 
    contrast_range, flip_horizontal, translation_range
):
    """Create TensorFlow augmentation pipeline"""
    layers = []
    
    if flip_horizontal:
        layers.append(tf.keras.layers.RandomFlip("horizontal"))
    
    if rotation_range > 0:
        layers.append(tf.keras.layers.RandomRotation(rotation_range))
    
    if zoom_range > 0:
        layers.append(tf.keras.layers.RandomZoom(zoom_range))
    
    if translation_range > 0:
        layers.append(tf.keras.layers.RandomTranslation(translation_range, translation_range))
    
    if brightness_range > 0:
        layers.append(tf.keras.layers.RandomBrightness(brightness_range))
    
    if contrast_range > 0:
        layers.append(tf.keras.layers.RandomContrast(contrast_range))
    
    if layers:
        return tf.keras.Sequential(layers, name="augmentation")
    else:
        return None

# Sidebar Controls
st.sidebar.subheader("🔧 Augmentation Einstellungen")

# Basic Parameters
rotation_range = st.sidebar.slider("🔄 Rotation Range", 0.0, 0.5, 0.2, 0.05)
zoom_range = st.sidebar.slider("🔍 Zoom Range", 0.0, 0.4, 0.2, 0.05)
brightness_range = st.sidebar.slider("☀️ Brightness Range", 0.0, 0.4, 0.2, 0.05)
contrast_range = st.sidebar.slider("🌓 Contrast Range", 0.0, 0.4, 0.2, 0.05)
translation_range = st.sidebar.slider("↔️ Translation Range", 0.0, 0.3, 0.2, 0.05)
flip_horizontal = st.sidebar.checkbox("🔄 Horizontal Flip", value=True)

# Image Selection
st.sidebar.subheader("🖼️ Bild Auswahl")
image_source = st.sidebar.selectbox("Bildquelle", ["Zufällig", "Spezifische Klasse", "Spezifischer Index"])

if image_source == "Spezifische Klasse":
    selected_class = st.sidebar.selectbox("Klasse wählen", range(len(classes)), 
                                        format_func=lambda x: f"{x}: {classes[x]}")
    class_indices = np.where(y_train.flatten() == selected_class)[0]
    selected_image_idx = np.random.choice(class_indices)
elif image_source == "Spezifischer Index":
    selected_image_idx = st.sidebar.number_input("Bild Index", 0, len(x_train)-1, 42)
else:
    selected_image_idx = np.random.randint(0, len(x_train))

# Number of augmentations to show
num_augmentations = st.sidebar.slider("Anzahl Augmentationen", 4, 16, 8)

# Create augmentation pipeline
augment_pipeline = create_augmentation_pipeline(
    rotation_range, zoom_range, brightness_range,
    contrast_range, flip_horizontal, translation_range
)

# Main Content
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<h2 class="sub-header">🖼️ Original Bild</h2>', unsafe_allow_html=True)
    
    # Get selected image
    original_image = x_train[selected_image_idx]
    original_label = classes[y_train[selected_image_idx][0]]
    
    # Display original
    fig_orig, ax_orig = plt.subplots(figsize=(6, 6))
    ax_orig.imshow(original_image)
    ax_orig.set_title(f'Original: {original_label}', fontsize=14, fontweight='bold')
    ax_orig.axis('off')
    st.pyplot(fig_orig)
    
    # Image info
    st.markdown(f"""
    <div class="info-box">
        <strong>📊 Bild Informationen:</strong><br>
        • Klasse: {original_label}<br>
        • Index: {selected_image_idx}<br>
        • Größe: {original_image.shape}<br>
        • Datentyp: {original_image.dtype}<br>
        • Wertebereich: {original_image.min():.3f} - {original_image.max():.3f}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<h2 class="sub-header">🎨 Augmentierte Versionen</h2>', unsafe_allow_html=True)
    
    if augment_pipeline is not None:
        # Create augmented versions
        cols_per_row = 4
        rows = (num_augmentations + cols_per_row - 1) // cols_per_row
        
        fig_aug, axes = plt.subplots(rows, cols_per_row, figsize=(16, 4*rows))
        if rows == 1:
            axes = axes.reshape(1, -1)
        
        for i in range(num_augmentations):
            row = i // cols_per_row
            col = i % cols_per_row
            
            # Apply augmentation
            augmented = augment_pipeline(tf.expand_dims(original_image, 0), training=True)
            augmented = tf.squeeze(augmented, 0)
            
            axes[row, col].imshow(augmented)
            axes[row, col].set_title(f'Augmented {i+1}', fontsize=10)
            axes[row, col].axis('off')
        
        # Hide unused subplots
        for i in range(num_augmentations, rows * cols_per_row):
            row = i // cols_per_row
            col = i % cols_per_row
            axes[row, col].axis('off')
        
        plt.tight_layout()
        st.pyplot(fig_aug)
        
    else:
        st.warning("🚨 Keine Augmentation Parameter ausgewählt!")

# Advanced Analysis Section
st.markdown('<h2 class="sub-header">📊 Augmentation Analyse</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 Parameter Übersicht")
    params_df = pd.DataFrame({
        'Parameter': ['Rotation', 'Zoom', 'Brightness', 'Contrast', 'Translation', 'Horizontal Flip'],
        'Wert': [rotation_range, zoom_range, brightness_range, contrast_range, translation_range, flip_horizontal],
        'Aktiv': [rotation_range > 0, zoom_range > 0, brightness_range > 0, 
                 contrast_range > 0, translation_range > 0, flip_horizontal]
    })
    st.dataframe(params_df, use_container_width=True)

with col2:
    st.markdown("### 📈 Augmentation Impact")
    
    # Calculate augmentation intensity
    intensity_score = (
        rotation_range * 2 +
        zoom_range * 2 +
        brightness_range * 2 +
        contrast_range * 2 +
        translation_range * 2 +
        (0.2 if flip_horizontal else 0)
    )
    
    # Create gauge chart
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = intensity_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Augmentation Intensität"},
        delta = {'reference': 1.0},
        gauge = {
            'axis': {'range': [None, 3]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 1], 'color': "lightgray"},
                {'range': [1, 2], 'color': "gray"},
                {'range': [2, 3], 'color': "red"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 2.5}}))
    
    fig_gauge.update_layout(height=300)
    st.plotly_chart(fig_gauge, use_container_width=True)

with col3:
    st.markdown("### 🎨 Transformation Types")
    
    active_transforms = []
    if rotation_range > 0:
        active_transforms.append("🔄 Rotation")
    if zoom_range > 0:
        active_transforms.append("🔍 Zoom")
    if brightness_range > 0:
        active_transforms.append("☀️ Brightness")
    if contrast_range > 0:
        active_transforms.append("🌓 Contrast")
    if translation_range > 0:
        active_transforms.append("↔️ Translation")
    if flip_horizontal:
        active_transforms.append("🔄 Horizontal Flip")
    
    for transform in active_transforms:
        st.markdown(f"✅ {transform}")
    
    if not active_transforms:
        st.markdown("❌ Keine Transformationen aktiv")

# Dataset Statistics
st.markdown('<h2 class="sub-header">📊 CIFAR-10 Dataset Statistiken</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Class distribution
    unique, counts = np.unique(y_train, return_counts=True)
    
    fig_dist = px.bar(
        x=[classes[i] for i in unique],
        y=counts,
        title="Klassenverteilung im Trainingsdatensatz",
        labels={'x': 'Klasse', 'y': 'Anzahl Bilder'},
        color=counts,
        color_continuous_scale='viridis'
    )
    fig_dist.update_layout(showlegend=False)
    st.plotly_chart(fig_dist, use_container_width=True)

with col2:
    # Dataset metrics
    st.markdown("### 📈 Dataset Metriken")
    
    metrics_data = {
        "Metrik": ["Training Images", "Test Images", "Klassen", "Bildgröße", "Kanäle"],
        "Wert": [len(x_train), len(x_test), len(classes), "32x32", 3]
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    st.dataframe(metrics_df, use_container_width=True)
    
    # Memory usage
    train_size_mb = x_train.nbytes / (1024**2)
    test_size_mb = x_test.nbytes / (1024**2)
    
    st.markdown(f"""
    <div class="metric-card">
        <strong>💾 Speicherverbrauch</strong><br>
        Training: {train_size_mb:.1f} MB<br>
        Test: {test_size_mb:.1f} MB
    </div>
    """, unsafe_allow_html=True)

# Best Practices Section
st.markdown('<h2 class="sub-header">💡 Data Augmentation Best Practices</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="augmentation-box">
        <h4>✅ Do's</h4>
        <ul>
            <li>Start mit moderaten Parametern</li>
            <li>Teste verschiedene Kombinationen</li>
            <li>Achte auf realistische Transformationen</li>
            <li>Validiere Performance mit Validation Set</li>
            <li>Nutze Domain-spezifische Augmentationen</li>
            <li>Kombiniere geometrische und photometrische Transforms</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="augmentation-box">
        <h4>❌ Don'ts</h4>
        <ul>
            <li>Übertreibung bei Parametern vermeiden</li>
            <li>Nicht alle Transformationen gleichzeitig</li>
            <li>Keine unrealistischen Verzerrungen</li>
            <li>Label-Changing Transforms vermeiden</li>
            <li>Nicht nur auf Training Set optimieren</li>
            <li>Computational Cost beachten</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Interactive Tips
if st.button("🎲 Zufällige Parameter generieren"):
    try:
        st.rerun()
    except Exception:
        pass

st.markdown("---")
st.markdown("**🎓 IU Data Analytics & Big Data Course - Week 6.3: Data Augmentation**")
st.markdown("Experimentieren Sie mit verschiedenen Parametern um die Auswirkungen von Data Augmentation zu verstehen!")
