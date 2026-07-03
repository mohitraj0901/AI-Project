# 🌱 AgroTech AI – Smart Agriculture Assistant

🚀 **Live Demo:** https://ai-project-13.onrender.com/  
🔗 **GitHub Repo:** https://github.com/mohitraj0901/AI-Project  

---

## 📌 Overview

AgroTech AI is a **Machine Learning powered smart agriculture web application** that helps farmers make data-driven decisions by recommending suitable crops and irrigation techniques based on soil nutrients and environmental conditions.

The application uses **Random Forest Machine Learning models** integrated with a **Flask backend** to provide real-time predictions.

---

# 🚀 Features

## 🌾 Crop Recommendation

Predicts the best suitable crop using:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Output:

- Recommended Crop (Rice, Wheat, Cotton, Maize, etc.)

---

## 💧 Irrigation Prediction

Suggests suitable irrigation techniques based on:

- Soil Type
- Crop Type
- Average Temperature
- Moisture Level
- Geographical Location

Output examples:

- Drip Irrigation
- Sprinkler Irrigation
- Surface Irrigation

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- Flask-CORS

## Frontend

- HTML5
- CSS3
- JavaScript

## Machine Learning

- scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

## Deployment

- Docker
- Render

---

# 🤖 Machine Learning Workflow


## 🌾 Crop Recommendation Model

Dataset:

- Kaggle Crop Recommendation Dataset

Features:

```
N
P
K
Temperature
Humidity
pH
Rainfall
```

Model:

```
Random Forest Classifier
```

Output:

```
Recommended Crop
```

Performance:

```
Accuracy: ~99%
```

---

## 💧 Irrigation Prediction Model


Features:

```
Soil Type
Crop Type
Average Temperature
Moisture Level
Location
```

Model:

```
Random Forest Classifier
```

Output:

```
Recommended Irrigation Technique
```

---

# ⚙️ Backend Architecture


```
User Input

      |
      |
      v

 Flask API

      |
      |

 ------------------------

 |                      |

Crop Model        Irrigation Model

(Random Forest)   (Random Forest)

      |
      |
 Prediction Response
```

The trained models are saved using **Joblib serialization**.

Flask loads the `.pkl` models and provides predictions using REST APIs.

---

# 📁 Project Structure


```
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
├── static/
│
├── Dockerfile
├── requirements.txt
└── README.md

```

---

# ⚠️ Challenges Faced

- Processing agricultural datasets
- Encoding categorical features
- Training accurate ML models
- Connecting ML models with Flask APIs
- Deploying ML application on cloud

---

# 🔮 Future Improvements

- Real-time weather API integration
- Satellite based crop monitoring
- Plant disease detection using Computer Vision
- Voice assistant for farmers
- Regional language support
- Larger real-world agricultural datasets

---

# ▶️ Run Locally


Clone the repository

```bash
git clone https://github.com/mohitraj0901/AI-Project
```


Move to project folder

```bash
cd AI-Project
```


Install dependencies

```bash
pip install -r requirements.txt
```


Run Flask application

```bash
python flask_web_app.py
```

---

# 👨‍💻 Developer

**Mohit Raj**

B.Tech CSE (AI & Data Science)  
Indian Institute of Information Technology Ranchi

