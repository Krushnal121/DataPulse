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
