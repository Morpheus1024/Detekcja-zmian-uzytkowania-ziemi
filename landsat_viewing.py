import os
import earthpy.plot as ep
import earthpy.spatial as es
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Define the directory where your images are stored
image_directory = 'zdjecie1'

# List of Landsat bands to load (adjust the names according to your files)
bands = [
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B1.TIF",
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B2.TIF",
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B3.TIF",
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B4.TIF",
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B5.TIF",
     "LE07_L2SP_190022_20190830_20200824_02_T1_SR_B7.TIF"
]

# Load each band as an array
band_paths = [os.path.join(image_directory, band) for band in bands]

# Stack bands to create a multi-band array
stacked_array, meta = es.stack(band_paths)

# Save the stacked array as a new multi-band GeoTIFF
output_path = os.path.join(image_directory, 'stacked_landsat.tif')

with rasterio.open(
    output_path,
    'w',
    driver='GTiff',
    height=stacked_array.shape[1],
    width=stacked_array.shape[2],
    count=stacked_array.shape[0],
    dtype=stacked_array.dtype
) as dst:
    for i in range(stacked_array.shape[0]):
        dst.write(stacked_array[i, :, :], i + 1)

print(f"Stacked image saved to {output_path}")

# Plot a False Color Composite using bands 5 (NIR), 4 (Red), and 3 (Green)
# Adjust the indices based on your specific bands order (here: 4, 3, 2)
ep.plot_rgb(stacked_array, rgb=(4, 3, 2), stretch=True, title='Landsat False Color Composite (NIR, Red, Green)')
plt.show()
