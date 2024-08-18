from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the model
model = joblib.load("../Model_Training/model.pkl")

# Initialize Flask app
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    species = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
    # Make prediction
    prediction = model.predict(features)
    print(prediction)
    return jsonify({'prediction':species[prediction[0]]})


if __name__ == '__main__':
    app.run(debug=True)
