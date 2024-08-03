"""# Install required libraries
!pip install azure-cognitiveservices-vision-customvision

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

# Set up Custom Vision credentials
ENDPOINT = "https://<your-endpoint>.cognitiveservices.azure.com/"
TRAINING_KEY = "<your-training-key>"
PREDICTION_KEY = "<your-prediction-key>"

# Create training client
credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_KEY})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
project = trainer.create_project("My Custom Vision Project")

# Add tags
tag = trainer.create_tag(project.id, "Tag1")

# Upload and tag images
import os
for image in os.listdir("path_to_images"):
    with open(f"path_to_images/{image}", "rb") as image_data:
        trainer.create_images_from_data(project.id, image_data.read(), tag_ids=[tag.id])

# Train the model
iteration = trainer.train_project(project.id)
trainer.update_iteration(project.id, iteration.id, is_default=True)

# Predict new images
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open("path_to_new_image.jpg", "rb") as image_data:
    results = predictor.classify_image(project.id, iteration.id, image_data.read())

# Display results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")
"""