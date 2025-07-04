# 🔧 Predictive Maintenance Web App (Flask)

This web application allows users to input machine metrics through a user-friendly form and receive predictions about potential tool failures. The backend is powered by a trained machine learning pipeline using XGBoost, deployed using Flask.

---

## 🚀 Features

- 🧠 Predicts whether a machine is likely to fail based on input parameters
- 📝 Form-based UI with dropdowns and numeric inputs
- 🔒 Built using Flask for lightweight backend deployment
- 📦 Uses a saved `xgb_pipeline_model.pkl` pipeline
- HTML + CSS interface for a clean UI

---

## 🧪 Input Features Expected by the Model

| Feature                    | Type     | Description                         |
|----------------------------|----------|-------------------------------------|
| `Type`                     | Categorical (`L`, `M`, `H`) | Machine type                       |
| `Air temperature [K]`      | Float    | Surrounding air temperature in Kelvin |
| `Process temperature [K]`  | Float    | Internal temperature in Kelvin       |
| `Rotational speed [rpm]`   | Float    | Speed of the rotating part (RPM)     |
| `Torque [Nm]`              | Float    | Torque applied to the machine        |
| `Tool wear [min]`          | Float    | Minutes the tool has been used       |

---

## 📦 How to Run the Flask App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/predictive-maintenance.git
   cd predictive-maintenance/webapp
Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies

```bash
pip install -r ../requirements.txt
```
Run the Flask server

```bash
python app.py
Open in your browser
Visit http://127.0.0.1:5000
```

```
🗂 Folder Structure
```text
predictive_maintenance_Web_App/
│
├── templates/
│   └── index.html            # Main form and result display
├── app.py                # Main Flask application
├── model
   ├── xgb_pipeline_model.pkl    # Trained pipeline model
├── requirements.txt
├── procfile
└── README.md                 # You're here!
```
⚠️ Notes
Input field names must match the model’s expected feature names.

Make sure the model file is a full pipeline (encoder + model) or the app will throw an error.

The form uses the POST method to send input values to the server for prediction.

✅ Prediction Output
Failure: Model predicts tool failure.

No Failure: Model predicts machine is running normally.

👨‍💻 Author
Durdana Khalid
Data Science Portfolio Project
GitHub: @DurdanaKhalid49

📜 License
Distributed under the MIT License. See LICENSE in the root folder.
