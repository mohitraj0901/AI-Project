# 🌱 AgroTech AI – Smart Agriculture Assistant

🚀 **Live Demo:** https://ai-project-13.onrender.com/  
🔗 **GitHub Repo:** https://github.com/mohitraj0901/AI-Project  

---

## 📌 Overview

AgroTech AI is a **Machine Learning powered smart agriculture web application** that helps farmers make data-driven decisions by recommending suitable crops and irrigation techniques based on soil nutrients and environmental conditions.

The system uses **Random Forest Machine Learning models** integrated with a Flask backend to provide real-time predictions through an interactive web interface.

---

## 🚀 Features

🌾 **Crop Recommendation System**
- Predicts the most suitable crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - Soil pH
  - Rainfall

💧 **Irrigation Prediction System**
- Suggests suitable irrigation methods:
  - Drip Irrigation
  - Sprinkler Irrigation
  - Surface Irrigation
  - Pivot Irrigation

Based on:
- Soil type
- Crop type
- Temperature
- Moisture level
- Geographical location

📊 **User-Friendly Interface**
- Simple web interface designed for easy agricultural decision-making.

---

## 🧠 Tech Stack

### Backend
- Python
- Flask
- Flask-CORS

### Frontend
- HTML5
- CSS3
- JavaScript

### Machine Learning
- scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

### Deployment
- Docker
- Render

---

## 🤖 Machine Learning Workflow


### 🌾 Crop Recommendation Model

Dataset:
- Kaggle Crop Recommendation Dataset

Features:


Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH
Rainfall


Model:


Random Forest Classifier


Output:


Recommended Crop
(Rice, Wheat, Cotton, Maize, etc.)


Model Performance:


Accuracy: ~99%



---

### 💧 Irrigation Prediction Model

Features:


Soil Type
Crop Type
Average Temperature
Moisture Level
Location


Output:


Recommended Irrigation Technique


Examples:


Drip Irrigation
Sprinkler Irrigation
Surface Irrigation



---

## ⚙️ Backend Architecture

User Input
|
|
Flask API
|

| |
Crop Model Irrigation Model
(Random Forest) (Random Forest)

 |

Prediction Response


Models are trained separately and saved using **Joblib serialization**.

The Flask backend loads the trained `.pkl` models and provides predictions through REST APIs.

---

## 📁 Project Structure



AI-Project/

│
├── flask_web_app.py
│
├── Crop_recommendation.csv
├── irrigation_data.csv
│
├── crop_r_m_training_and_saving.py
├── irrigationmodel.py
│
├── crop_recommendation_model.pkl
├── irrigation_model.pkl
├── label_encoders.pkl
│
├── templates/
│
├── static/
│
├── Dockerfile
├── requirements.txt
└── README.md


---

## ⚠️ Challenges Faced

- Processing categorical agricultural features
- Encoding crop, soil and location data
- Selecting suitable ML algorithms
- Integrating ML models with Flask APIs
- Deploying ML-based application on cloud

---

## 🔮 Future Improvements

- Integration with real-time weather APIs
- Satellite-based crop monitoring
- Plant disease detection using Computer Vision
- Voice assistant support for farmers
- Regional language support
- Larger real-world agricultural datasets

---

## ▶️ Run Locally


Clone repository

```bash
git clone https://github.com/mohitraj0901/AI-Project

Move into project folder

cd AI-Project

Install dependencies

pip install -r requirements.txt

Run Flask application

python flask_web_app.py
👨‍💻 Developer

Mohit Raj
B.Tech CSE (AI & Data Science)
IIIT Ranchi
