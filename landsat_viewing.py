import os
import earthpy.plot as ep
import earthpy.spatial as es
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the directory where your images are stored
image_directory = 'data3'

# List of Landsat bands to load (adjust the names according to your files)
# List of desired band suffixes
band_suffixes = ["B1", "B2", "B3", "B4", "B5", "B6", "B7"]

# Function to check if a file ends with one of the band suffixes
def is_desired_band(filename):
    return any(filename.endswith(suffix + ".TIF") for suffix in band_suffixes)

# List of Landsat bands to load based on the desired suffixes
bands = [file for file in os.listdir(image_directory) if is_desired_band(file)]

# Sort the bands list to ensure correct order
bands.sort()

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


# Function to save smaller sections of the image
def save_image_sections(stacked_array, output_dir, section_size=(512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the number of sections along each dimension
    num_rows = stacked_array.shape[1] // section_size[0]
    num_cols = stacked_array.shape[2] // section_size[1]

    # Normalize the uint16 array to uint8
    def normalize_to_uint8(array):
        array_min, array_max = array.min(), array.max()
        return ((array - array_min) / (array_max - array_min) * 255).astype(np.uint8)

    # Loop through each section and save it
    for i in range(num_rows):
        for j in range(num_cols):
            section = stacked_array[:, i * section_size[0]:(i + 1) * section_size[0],
                      j * section_size[1]:(j + 1) * section_size[1]]
            section_rgb = np.dstack([section[4], section[3], section[2]])
            section_rgb_normalized = normalize_to_uint8(section_rgb)
            section_path = os.path.join(output_dir, f'section_{i}_{j}.png')
            plt.imsave(section_path, section_rgb_normalized)
            print(f"Section saved to {section_path}")


# Save sections of the image
output_sections_dir = os.path.join(image_directory, 'sections')
save_image_sections(stacked_array, output_sections_dir)
