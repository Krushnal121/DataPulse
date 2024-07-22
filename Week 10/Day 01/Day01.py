import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an example image
image = cv2.imread('example.jpg', 0)

# Image Filtering: Applying a Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Edge Detection: Using Canny Edge Detector
edges = cv2.Canny(image, 100, 200)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(blurred_image, cmap='gray'), plt.title('Blurred Image')
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Edge Detection')
plt.show()
