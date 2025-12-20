import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def show_image(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')

# 1. Ein künstliches Bild erstellen
# Ein helles Quadrat auf dunklem Grund
image = np.zeros((10, 10))
image[2:8, 2:8] = 1.0

print("Original Bild Shape:", image.shape)

# 2. Filter definieren

# Vertikaler Kanten-Detektor (Sobel-artig)
# Links positiv, rechts negativ -> reagiert auf vertikale Kanten
kernel_vertical = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Horizontaler Kanten-Detektor
# Oben positiv, unten negativ -> reagiert auf horizontale Kanten
kernel_horizontal = np.array([
    [ 1,  1,  1],
    [ 0,  0,  0],
    [-1, -1, -1]
])

# 3. Convolution anwenden
# mode='valid': Keine Padding, Bild wird kleiner (8x8)
feature_map_v = convolve2d(image, kernel_vertical, mode='valid')
feature_map_h = convolve2d(image, kernel_horizontal, mode='valid')

# 4. Visualisierung
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
show_image(image, "Original (10x10)")

plt.subplot(1, 3, 2)
show_image(feature_map_v, "Vertikale Kanten (Feature Map)")
# Man sieht: Linke Kante ist hell (positiv), rechte Kante dunkel (negativ)

plt.subplot(1, 3, 3)
show_image(feature_map_h, "Horizontale Kanten (Feature Map)")
# Man sieht: Obere Kante hell, untere Kante dunkel

print("Plot wird erstellt...")
plt.tight_layout()
plt.show()

print("\n--- Analyse ---")
print(f"Shape nach Convolution (valid): {feature_map_v.shape}")
print("Beobachtung: Die Feature Maps 'leuchten' dort auf, wo das Muster des Filters im Bild gefunden wurde.")

# 5. Max Pooling Simulation (Manuell)
print("\n--- Max Pooling (2x2) ---")
# Wir nehmen einfachheitshalber einen Ausschnitt
block = feature_map_v[0:2, 0:2]
print(f"2x2 Block aus Feature Map:\n{block}")
pooled_val = np.max(block)
print(f"Max Pooled Wert: {pooled_val}")