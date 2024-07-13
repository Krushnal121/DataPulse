import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess a sample of the training dataset
sample_train_data = {
    'Loan_ID': ['LP001002', 'LP001003', 'LP001005'],
    'Gender': ['Male', 'Male', 'Male'],
    'Married': ['No', 'Yes', 'Yes'],
    'Dependents': ['0', '1', '0'],
    'Education': ['Graduate', 'Graduate', 'Not Graduate'],
    'Self_Employed': ['No', 'No', 'Yes'],
    'ApplicantIncome': [5849, 4583, 3000],
    'CoapplicantIncome': [0.0, 1508.0, 0.0],
    'LoanAmount': [128.0, 128.0, 66.0],
    'Loan_Amount_Term': [360.0, 360.0, 360.0],
    'Credit_History': [1.0, 1.0, 1.0],
    'Property_Area': ['Urban', 'Rural', 'Urban'],
    'Loan_Status': ['Y', 'N', 'Y']
}
df = pd.DataFrame(sample_train_data)

# Preprocess data
def preprocess_data(df):
    label_encoder = LabelEncoder()
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)
    return df

df = preprocess_data(df)

# Prepare training data
X = df.drop(columns=['Loan_ID', 'Loan_Status'])
y = df['Loan_Status'].apply(lambda x: 1 if x == 'Y' else 0)

# Split the data
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Train a RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy: {accuracy:.2f}")

# Predict on the sample validation set and show results
print("Predictions:", y_pred)
