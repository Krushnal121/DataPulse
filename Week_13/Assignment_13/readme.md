# Project Report: Iris Species Classification Model with Flask API Deployment on Azure

## 1. **Introduction**
### 1.1 **Project Overview**
This project involves developing a machine learning model to classify the species of the Iris flower based on sepal and petal dimensions. The model is trained using the famous Iris dataset. Once trained, the model is deployed on a Linux instance on Azure, and an API is created using Flask to facilitate predictions.

### 1.2 **Objectives**
- Train a machine learning model to classify Iris species.
- Deploy the trained model on a Linux instance in Azure.
- Develop a RESTful API using Flask to expose the model for prediction requests.

## 2. **Dataset and Model Training**
### 2.1 **Dataset**
The Iris dataset consists of 150 samples with the following features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Each sample belongs to one of the three species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

### 2.2 **Model Training**
#### 2.2.1 **Model Selection**
The model chosen for this task is a Support Vector Machine (SVM) classifier, which is suitable for classification tasks and performs well with small to medium-sized datasets.

#### 2.2.2 **Training Process**
1. **Import Necessary Libraries**:
    ```python
    import numpy as np
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    import joblib
    ```

2. **Load the Iris Dataset**:
    ```python
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    ```

3. **Split the Data into Training and Testing Sets**:
    ```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    ```

4. **Train the SVM Model**:
    ```python
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    ```

5. **Evaluate the Model**:
    ```python
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy}")
    ```

6. **Save the Trained Model**:
    ```python
    joblib.dump(model, "model.pkl")
    ```

### 2.3 **Model Evaluation**
The model was evaluated on the test set, achieving an accuracy of approximately 97%. The model was then saved as `model.pkl` for deployment.

## 3. **Deployment on Azure**
### 3.1 **Setting Up a Linux Instance on Azure**
#### 3.1.1 **Create a Virtual Machine**
1. **Navigate to Azure Portal** and create a new virtual machine (VM).
2. **Choose the Operating System**: Select a Linux distribution such as Ubuntu 20.04.
3. **Select the VM Size**: Choose an appropriate size depending on the workload.
4. **Configure Networking**: Ensure the VM is accessible via SSH and has a public IP.
5. **Review and Launch** the VM.

#### 3.1.2 **Access the VM via SSH**
After the VM is launched, connect to it via SSH:
```bash
ssh username@your_vm_public_ip
```

### 3.2 **Setting Up the Environment**
#### 3.2.1 **Install Dependencies**
Once connected to the VM, install the necessary packages:
```bash
sudo apt update
sudo apt install python3-pip python3-venv
pip3 install flask joblib numpy scikit-learn
```

#### 3.2.2 **Transfer the Model to the VM**
Upload the `model.pkl` file to the VM using SCP or any other file transfer method:
```bash
scp model.pkl username@your_vm_public_ip:/path/to/directory/
```
Or just clone your git repository:
```bash
git clone <"your repository url">
```


### 3.3 **Developing the Flask API**
#### 3.3.1 **Flask Application**
Create a Flask application to expose the model as a RESTful API:
```python
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
    app.run(host='0.0.0.0', port=5000)
```

#### 3.3.2 **Running the Flask App**
Run the Flask application:
```bash
python3 app.py
```
This starts the API server, which listens on port 5000 for incoming prediction requests.

### 3.4 **Testing the API**
You can test the API using `curl` or Postman:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}' \
http://your_vm_public_ip:5000/predict
```
The API will return the predicted species as a JSON response.

## 4. Project Demo

### 01. Creation of Linux Instance on Azure.
![Screenshot 2024-08-18 185403.png](Images%2FScreenshot%202024-08-18%20185403.png)

### 02. Incoming Traffic on Flask API Server.
![Screenshot 2024-08-18 193921.png](Images%2FScreenshot%202024-08-18%20193921.png)

### 03. Testing Deployed API with Postman
![Screenshot (102).png](Images%2FScreenshot%20%28102%29.png)
![Screenshot (101).png](Images%2FScreenshot%20%28101%29.png)
![Screenshot (100).png](Images%2FScreenshot%20%28100%29.png)
![Screenshot (99).png](Images%2FScreenshot%20%2899%29.png)

## 5. **Conclusion**
This project demonstrates the end-to-end process of developing a machine learning model for classifying Iris species and deploying it as an API on a Linux instance in Azure. The model can be accessed via a RESTful API, making it easy to integrate with other applications for real-time predictions.
