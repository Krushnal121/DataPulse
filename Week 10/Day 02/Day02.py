# Image Transformation: Rotating the image
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('example.jpg', 0)
rows, cols = image.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_image = cv2.warpAffine(image, M, (cols, rows))

# Image Enhancement: Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(rotated_image, cmap='gray'), plt.title('Rotated Image')
plt.subplot(1, 2, 2), plt.imshow(equalized_image, cmap='gray'), plt.title('Equalized Image')
plt.show()
