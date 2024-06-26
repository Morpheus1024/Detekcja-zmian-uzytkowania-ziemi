# Project Phase Report: Data Retrieval and Initial Processing

## Introduction

The goal of this project phase was to select and load satellite images with good visibility of changes. This process involved collaborating with data processing teams, creating an account on the Earthexplorer platform, and selecting cloud-free images from the Landsat 8 satellite. Additionally, Python code was developed to load images in .TIF and .jpg formats, as well as to split the images into smaller sections.

## Tasks Completed

### 1. Selection of Satellite and Images with Low Cloud Coverage

On the Earthexplorer platform, the Landsat 8-9 satellite was chosen to download images without distortions and black bands. The downloaded images are from the years 2013-2024. The search engine provided by the service was used to select images with cloud coverage below 10% to ensure good visibility. It was essential to select images from similar times of the year and day.

#### Process

1. Creating an account on the Earthexplorer platform.
2. Selecting images of key areas with good visibility.

<img src="https://github.com/Morpheus1024/Detekcja-zmian-uzytkowania-ziemi/assets/108287744/c4975466-4bbf-4cd3-9e78-579dfaa817fb" alt="Earthexplorer" height="250">

### 2. Downloading Images

After selecting the images, they were downloaded in .TIF and .jpg formats.

#### Process

1. Selecting image packages with channels in .TIF format and images in .jpg format.
2. Downloading the images as Bulk Download.

### 3. Loading Images in Different Formats

Code was written to load and display the images.

#### Process

1. Writing the part responsible for loading individual .TIF channels.
2. Combining the channels to obtain a colored image of the area in good resolution.

```python
stacked_array, meta = es.stack(band_paths)
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
```

3. Adding lines responsible for loading the image with the .jpg extension.

<img src="https://github.com/Morpheus1024/Detekcja-zmian-uzytkowania-ziemi/assets/108287744/28d75f03-b8e9-4d36-916a-2b6d5ac79094" alt="Earthexplorer" height="250">

### 4. Image Fragmentation

Due to the large image size, the image was divided into smaller sections to facilitate easier analysis or the ability to adjust the code for extracting key sections of images, e.g., areas with the most significant changes.

#### Process

1. Specifying the final sizes of the small sections.
2. Dividing into smaller sections of the specified size and saving them to the output folder.

```python
    for i in range(num_rows):
        for j in range(num_cols):
            section = stacked_array[:, i * section_size[0]:(i + 1) * section_size[0],
                      j * section_size[1]:(j + 1) * section_size[1]]
            section_rgb = np.dstack([section[4], section[3], section[2]])
            section_rgb_normalized = normalize_to_uint8(section_rgb)
            section_path = os.path.join(output_dir, f'section_{i}_{j}.png')
            plt.imsave(section_path, section_rgb_normalized)
            print(f"Section saved to {section_path}")
```

## Summary

In this project phase, tasks related to the retrieval and initial processing of satellite images were completed. The download and processing of images provided us with high-quality data that will be used in further analyses. Checking image transparency and managing data versions in the Git repository provide a solid foundation for continuing work on the project.
