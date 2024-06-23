import rasterio
import matplotlib.pyplot as plt
import numpy as np
import earthpy.plot as ep

# Ścieżka do zapisanego pliku .tif
file_path = 'data2/stacked_landsat.tif'

# Otwórz obraz
with rasterio.open(file_path) as src:
    # Czytaj kanały 5 (NIR), 4 (Red) i 3 (Green)
    band5 = src.read(5)  # Kanał 5 (NIR)
    band4 = src.read(4)  # Kanał 4 (Red)
    band3 = src.read(3)  # Kanał 3 (Green)

# Normalizowanie kanałów do zakresu 0-1 dla lepszego wyświetlania
def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

band5 = normalize(band5)
band4 = normalize(band4)
band3 = normalize(band3)

# Połącz kanały w obraz RGB
rgb_image = np.dstack((band5, band4, band3))

# Wyświetl obraz False Color Composite
plt.imshow(rgb_image)
plt.title('Landsat False Color Composite (NIR, Red, Green)')
plt.axis('off')
plt.show()

