# Install required libraries
!pip install azure-cognitiveservices-vision-customvision

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Set up Custom Vision credentials
ENDPOINT = "https://<your-endpoint>.cognitiveservices.azure.com/"
PREDICTION_KEY = "<your-prediction-key>"
PROJECT_ID = "<your-project-id>"
PUBLISH_ITERATION_NAME = "<your-iteration-name>"

credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

# Load image and predict
with open("path_to_image.jpg", "rb") as image_data:
    results = predictor.classify_image(PROJECT_ID, PUBLISH_ITERATION_NAME, image_data)

# Display results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")


# Install required libraries
!pip install opencv-python

import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('path_to_image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.show()

# Perform edge detection
edges = cv2.Canny(image, 100, 200)

# Display edges
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.show()
