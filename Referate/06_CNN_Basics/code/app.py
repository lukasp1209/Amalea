import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title("Unit 06: CNN Filter Explorer")
st.markdown("Laden Sie ein Bild hoch und wenden Sie verschiedene **Convolutional Kernel** an, um zu sehen, wie Computer Merkmale extrahieren.")

# --- Sidebar ---
st.sidebar.header("Einstellungen")
filter_name = st.sidebar.selectbox(
    "Filter wählen",
    ["Original", "Edge Detection (Sobel X)", "Edge Detection (Sobel Y)", "Edge Detection (Laplacian)", "Sharpen", "Blur (Average)", "Emboss"]
)

uploaded_file = st.sidebar.file_uploader("Bild hochladen", type=["jpg", "png", "jpeg"])

# --- Filter Definitionen ---
def apply_filter(image, filter_type):
    # Bild in Graustufen konvertieren für einfachere Kanten-Erkennung
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    if filter_type == "Original":
        return image
    
    elif filter_type == "Edge Detection (Sobel X)":
        # Vertikale Kanten
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        return cv2.filter2D(gray, -1, kernel)
    
    elif filter_type == "Edge Detection (Sobel Y)":
        # Horizontale Kanten
        kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        return cv2.filter2D(gray, -1, kernel)
    
    elif filter_type == "Edge Detection (Laplacian)":
        # Alle Kanten
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        return cv2.filter2D(gray, -1, kernel)
    
    elif filter_type == "Sharpen":
        # Verstärkt die Mitte, zieht Nachbarn ab
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel) # Hier auf Farbe anwendbar
    
    elif filter_type == "Blur (Average)":
        # Mittelwertbildung (Weichzeichner)
        kernel = np.ones((5, 5), np.float32) / 25
        return cv2.filter2D(image, -1, kernel)
    
    elif filter_type == "Emboss":
        # Relief-Effekt
        kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
        return cv2.filter2D(gray, -1, kernel)
        
    return image

# --- Main App ---

if uploaded_file is not None:
    # Bild laden
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    st.subheader("Ergebnis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(img_array, caption="Original", use_container_width=True)
    
    with col2:
        processed_img = apply_filter(img_array, filter_name)
        st.image(processed_img, caption=f"Filter: {filter_name}", use_container_width=True)
        
    st.info(f"**Erklärung:** Der Filter '{filter_name}' wird als kleine Matrix (Kernel) über das Bild geschoben. Das Ergebnis ist eine Feature Map.")

else:
    st.info("Bitte laden Sie ein Bild in der Sidebar hoch.")