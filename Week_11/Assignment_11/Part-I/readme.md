# Report: Developing a Custom Vision Model using Azure Custom Vision for Image Classification

## 1. Introduction

### Objective
The objective of this project is to develop a custom vision model using Azure Custom Vision to classify images into specific categories. We will be using the Simpsons image dataset, which contains images of characters from the popular TV show "The Simpsons."

### Dataset Description
The Simpsons image dataset includes images of various characters from "The Simpsons." The dataset is divided into training, validation, and test sets. Each image is labeled with the character it represents.

### Tools and Technologies
- Azure Custom Vision
- Python
- OpenCV
- Matplotlib

## 2. Azure Custom Vision Model Development

### Step-by-Step Guide to Configuring Azure Custom Vision

#### Step 1: Create an Azure Custom Vision Resource
1. Sign in to the [Azure Portal](https://portal.azure.com/).
2. Click on "Create a resource."
3. Search for "Custom Vision" and select it.
4. Click on "Create."
5. Fill in the required details:
   - Subscription: Select your Azure subscription.
   - Resource Group: Create a new resource group or select an existing one.
   - Name: Enter a name for your Custom Vision resource.
   - Location: Select a location.
   - Pricing tier: Select the desired pricing tier.
6. Click on "Review + create" and then "Create."

#### Step 2: Create a Custom Vision Project
1. Go to the [Custom Vision portal](https://www.customvision.ai/).
2. Sign in with your Azure account.
3. Click on "New Project."
4. Fill in the project details:
   - Name: Enter a name for your project.
   - Description: Enter a description (optional).
   - Resource: Select the Custom Vision resource created in Step 1.
   - Project Type: Select "Classification."
   - Classification Types: Select "Multiclass" for single-label classification or "Multilabel" for multi-label classification.
   - Domains: Select the appropriate domain (e.g., General, Food, Landmarks, etc.).
5. Click on "Create Project."

#### Step 3: Upload and Tag Images
1. In the Custom Vision portal, go to your project.
2. Click on "Add images."
3. Upload images from the Simpsons dataset for training.
4. Tag each image with the appropriate character label.
5. Repeat the process for validation and test images.

#### Step 4: Train the Model
1. After uploading and tagging images, click on "Train" to start training the model.
2. Select the training type (Quick Training or Advanced Training).
3. Wait for the training to complete. The training process may take several minutes to hours, depending on the number of images and training type selected.

#### Step 5: Evaluate the Model
1. Once the model is trained, evaluate its performance using the validation set.
2. Check metrics such as precision, recall, and accuracy.
3. If necessary, adjust the training set and retrain the model to improve performance.

#### Step 6: Test the Model
1. Use the test set to test the model's performance.
2. Upload test images and check the predicted labels.

### Output Screenshots
![Model Performance Stats](Screenshot%202024-08-04%20144314.png)
![Output 01](Screenshot%202024-08-04%20143341.png)
![Output 02](Screenshot%202024-08-04%20143502.png)
![Output 03](Screenshot%202024-08-04%20143553.png)
![Output 04](Screenshot%202024-08-04%20143653.png)

## 3. Python Script for Image Histogram Analysis

### Introduction
In addition to developing the custom vision model, we performed image analysis using Python and OpenCV to calculate and plot histograms of color channels (RGB) for an image of a natural landscape to analyze color variations and intensities.

### Script

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the image
image_path = 'path_to_your_image.jpg'

# Check if the image path exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"The image path '{image_path}' does not exist. Please provide a valid path.")

image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise ValueError(f"Failed to load image. Please check if the file at '{image_path}' is a valid image.")

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Calculate the histogram for each color channel
channels = ('b', 'g', 'r')
hist_data = {}
for i, channel in enumerate(channels):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    hist_data[channel] = hist

# Plot histograms for each color channel
plt.figure(figsize=(14, 7))

for i, channel in enumerate(channels):
    plt.subplot(1, 3, i + 1)
    plt.plot(hist_data[channel], color=channel)
    plt.title(f'{channel.upper()} channel histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Advanced Visualization: 2D Histogram for color channels
plt.figure(figsize=(14, 7))

# Plotting 2D histogram for Red and Green channels
plt.subplot(1, 2, 1)
plt.hist2d(image_rgb[:, :, 0].ravel(), image_rgb[:, :, 1].ravel(), bins=32, range=[[0, 256], [0, 256]], cmap='Reds')
plt.colorbar()
plt.title('2D Histogram (Red vs Green)')
plt.xlabel('Red Intensity')
plt.ylabel('Green Intensity')

# Plotting 2D histogram for Green and Blue channels
plt.subplot(1, 2, 2)
plt.hist2d(image_rgb[:, :, 1].ravel(), image_rgb[:, :, 2].ravel(), bins=32, range=[[0, 256], [0, 256]], cmap='Greens')
plt.colorbar()
plt.title('2D Histogram (Green vs Blue)')
plt.xlabel('Green Intensity')
plt.ylabel('Blue Intensity')

plt.tight_layout()
plt.show()

# Advanced Visualization: Histogram Equalization
# Equalize the histogram for each channel
image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
image_equalized = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# Display the original and equalized images side by side
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(image_equalized)
plt.title('Histogram Equalized Image')

plt.tight_layout()
plt.show()
```

### Explanation
- **Histogram Calculation**: The script calculates and plots histograms for the red, green, and blue color channels of an image.
- **2D Histograms**: It also provides 2D histograms for the red-green and green-blue channel pairs.
- **Histogram Equalization**: The script demonstrates histogram equalization to enhance the image's contrast.

## 4. Conclusion

In this project, we successfully developed a custom vision model using Azure Custom Vision to classify images from the Simpsons dataset. Additionally, we performed advanced image analysis using OpenCV to calculate and visualize color histograms. The combination of these techniques demonstrates the power of computer vision in analyzing and understanding visual data.

## 5. Future Work

- **Model Improvement**: Continue to improve the model by adding more training data and refining the model parameters.
- **Deployment**: Deploy the model to a web or mobile application to provide real-time image classification.
- **Advanced Analytics**: Explore more advanced image processing techniques and integrate them into the analysis pipeline.

---

This report outlines the process and results of developing a custom vision model for image classification using Azure Custom Vision and performing advanced image analysis using Python and OpenCV.