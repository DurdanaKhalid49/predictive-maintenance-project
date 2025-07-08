from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load saved pipeline model
with open('model/xgb_pipeline_model.pkl', 'rb') as f:
    model = pickle.load(f)
# Home page with form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs (match names exactly from HTML)
        Type = request.form['Type']
        Air_temp = float(request.form['Air_temperature'])
        Process_temp = float(request.form['Process_temperature'])
        Speed = float(request.form['Rotational_speed'])
        Torque = float(request.form['Torque'])
        Wear = float(request.form['Tool_wear'])

        # Create DataFrame with correct column names (match training data)
        data = pd.DataFrame([{
            'Type': Type,
            'Air temperature [K]': Air_temp,
            'Process temperature [K]': Process_temp,
            'Rotational speed [rpm]': Speed,
            'Torque [Nm]': Torque,
            'Tool wear [min]': Wear
        }])

        # Predict using pipeline model
        prediction = model.predict(data)
        pred_text = "Failure" if prediction[0] == 1 else "No Failure"

        return render_template('index.html', prediction_text=f"Prediction: {pred_text}")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


