from flask import Flask, render_template
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import os


app = Flask(__name__)
CORS(app)


# ---------------- LOAD MODELS ----------------

# Irrigation model
irrigation_model = joblib.load("irrigation_model.pkl")
irrigation_label_encoders = joblib.load("label_encoders.pkl")


# Crop Recommendation model
crop_model = joblib.load("crop_recommendation_model.pkl")



# ---------------- HTML ROUTES ----------------


@app.route('/')
def index():
    return render_template(
        'index.html',
        bg_image='bg.jpg'
    )


@app.route('/crop_rotation')
def crop_rotation():
    return render_template(
        'crop_rotation.html',
        bg_image='bg2.jpg'
    )


@app.route('/irrigation')
def irrigation():
    return render_template(
        'irrigation.html',
        bg_image='bg3.jpg'
    )



# ---------------- IRRIGATION PREDICTION ----------------


@app.route("/predict", methods=["POST"])
def predict_irrigation():

    try:

        data = request.get_json()

        print(
            "Irrigation Received:",
            data
        )


        location = data["Geographical_Location"]
        crop = data["Crop_Type"]
        soil = data["Soil_Type"]

        temperature = float(
            data["Avg_Temperature"]
        )

        moisture = float(
            data["Moisture_Level"]
        )


        # Encoding categorical values

        soil_encoded = irrigation_label_encoders[
            "Soil_Type"
        ].transform([soil])[0]


        crop_encoded = irrigation_label_encoders[
            "Crop_Type"
        ].transform([crop])[0]


        location_encoded = irrigation_label_encoders[
            "Geographical_Location"
        ].transform([location])[0]



        input_features = np.array(
            [[
                soil_encoded,
                crop_encoded,
                temperature,
                moisture,
                location_encoded
            ]]
        )


        prediction = irrigation_model.predict(
            input_features
        )


        predicted_irrigation = (
            irrigation_label_encoders[
                "Irrigation_Type"
            ]
            .inverse_transform(prediction)[0]
        )


        return jsonify(
            {
                "Predicted_Irrigation_Type":
                predicted_irrigation
            }
        )


    except Exception as e:

        return jsonify(
            {
                "error":str(e)
            }
        ),400




# ---------------- CROP RECOMMENDATION ----------------


@app.route('/crop_recommendation', methods=['POST'])
def crop_recommendation():

    try:

        data = request.get_json()

        print(
            "Crop Data Received:",
            data
        )


        nitrogen = float(
            data["N"]
        )

        phosphorus = float(
            data["P"]
        )

        potassium = float(
            data["K"]
        )

        temperature = float(
            data["temperature"]
        )

        humidity = float(
            data["humidity"]
        )

        ph = float(
            data["ph"]
        )

        rainfall = float(
            data["rainfall"]
        )


        input_data = pd.DataFrame(
            [{
                "N": nitrogen,
                "P": phosphorus,
                "K": potassium,
                "temperature": temperature,
                "humidity": humidity,
                "ph": ph,
                "rainfall": rainfall
            }]
        )


        prediction = crop_model.predict(
            input_data
        )


        recommended_crop = prediction[0]


        print(
            "Recommended Crop:",
            recommended_crop
        )


        return jsonify(
            {
                "Recommended Crop":
                recommended_crop
            }
        )


    except Exception as e:

        return jsonify(
            {
                "error":str(e)
            }
        ),400





# ---------------- RUN APP ----------------


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )


    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )