import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg', 0)

# Morphological Operations: Dilation
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=1)

# For R-CNN, refer to specialized libraries such as PyTorch or TensorFlow
# Example: Using torchvision's Faster R-CNN
import torch
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn

model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Display the result of morphological operation
plt.imshow(dilated_image, cmap='gray'), plt.title('Dilated Image')
plt.show()
