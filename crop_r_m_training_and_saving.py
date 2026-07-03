# crop_r_m_training_and_saving.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


# Load dataset
data = pd.read_csv("Crop_recommendation.csv")


# Check dataset
print(data.head())


# Features
X = data[
    [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
]


# Target
y = data["label"]


# Train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Random Forest Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train

model.fit(
    X_train,
    y_train
)


# Test

prediction = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    prediction
)


print(
    "Model Accuracy:",
    accuracy * 100,
    "%"
)


# Save trained model

joblib.dump(
    model,
    "crop_recommendation_model.pkl"
)


print(
    "Model saved as crop_recommendation_model.pkl"
)