# Data Analysis

## Introduction

In our project, we focused on analyzing satellite data to investigate changes on the Earth's surface. Initially, we used images from the Landsat 7 satellite, but due to quality issues and image imperfections - see black bands on the left and right sides of the image - we switched to using images from the newer Landsat 8 satellite, which has been providing images since 2013. We conducted a detailed comparative analysis of these images to assess changes occurring in the studied area. This report presents the evolution of the satellite image analysis methodology.

## Methodology

### Using Landsat 7

At the beginning of the project, we used images from Landsat 7, which has been providing data since 1999. This satellite is equipped with the Enhanced Thematic Mapper Plus (ETM+). Our goal was to analyze changes in selected years. Unfortunately, we encountered significant issues with data quality. The biggest problem was the black bands on the downloaded images.

### Transition to Landsat 8

Due to the mentioned difficulties, we decided to use images from the Landsat 8 satellite, launched in 2013. This satellite is equipped with the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS), allowing for more detailed and precise data. The images from Landsat 8 did not have the issue with black bands, which significantly facilitated our analysis.

### Attempts to Use Image Analysis Models

Before proceeding to direct image comparison, we attempted to apply various image analysis models to automate the process. We tested models such as ResNet 50, ResNet 101, YOLO v8, YOLO v9, and five other models. Unfortunately, none of these models produced satisfactory results in the context of satellite data analysis from Landsat. The models struggled with accurately identifying changes in land cover, which forced us to change our approach.

### Analysis Based on Thresholding Segmentation

After abandoning the use of ready-made models, we developed another solution. The initial process consisted of the following stages:

1. Loading the appropriate images
2. Cropping the images to eliminate terrain shift
3. Calculating pixel differences, normalization, applying thresholding to display differences
4. Applying the K-Means algorithm to find dominant colors in the difference image
5. Assigning a class to the detected colors: forest, city, water, field

Example of the algorithm's operation on a rainforest image:

![image](https://github.com/knrdsmt/AWS-Klasyfikacja/assets/97449172/1c49f25b-2f75-4c2b-bbf9-06ecf149c2c6)

## Analysis Process

Ultimately, the analysis process was streamlined.

1. **Data Collection**: We started by collecting appropriate images from both satellites for selected years.
2. **Data Preparation and Preliminary Filtering**: We performed preliminary data processing, removing artifacts and calibrating images. Images unsuitable for analysis were discarded.
3. **Image Comparison Process**
   1. Identifying from the dataset two images representing the same area of Earth by decoding information found in the file names: reading the path, row, and year parameters. Determining which image is older and which is newer.
   2. Converting the image colors to grayscale, using the Oriented FAST and Rotated BRIEF algorithm to extract features, identifying similarity points using BFMacher.
   3. Calculating the homography matrix and aligning the images to eliminate terrain shift.
   4. Identifying the common area depicted in both images and cropping them.
   5. Calculating differences between the images, normalization, and reduction to a single channel.
   6. Change analysis
   7. Visualization of results: showing input images, heat maps, zooming in on the largest detected changes between the images.

![alt text](1.png)

## Conclusions

Our work demonstrated that switching to data from Landsat 8 was crucial for obtaining more reliable and accurate results. Thanks to the more modern sensors and better quality images, we could analyze changes on the Earth's surface more precisely. We found that direct image comparison proved to be the most effective analysis method, despite previous attempts to use various analytical models.

## PySpark

In addition to the task related to data analysis, we familiarized ourselves with PySpark, whose use was indicated in the project task description. We used it to aggregate the selected images and for partial data processing. PySpark was used both on a local machine and on a computing cluster in the AWS service. Our observations showed that using Spark accelerated the operations on the downloaded images.
