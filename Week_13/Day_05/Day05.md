### Day 5: Assignment - Model Deployment
---
**Overview:**
- **Topic:** Model Deployment
- **Objective:** Deploy a machine learning model using Azure services.

**Assignment Description:**
- **Task:** Deploy a pre-trained machine learning model (e.g., classification or regression) using Azure services such as Azure Functions or Azure App Service.
- **Steps:**
  1. **Prepare the Model:** Export the trained model in a suitable format (e.g., ONNX, TensorFlow, or PyTorch).
  2. **Develop the Deployment Code:** Write a Python script to load the model, process inputs, and return predictions.
  3. **Deploy the Model:** Use Azure Functions or Azure App Service to host the model and make it accessible via an API endpoint.
  4. **Test the Deployment:** Send test requests to the API to ensure the model is working correctly.

**Code Snippet:**
```python
from flask import Flask, request, jsonify
import joblib

# Load the model
model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
```