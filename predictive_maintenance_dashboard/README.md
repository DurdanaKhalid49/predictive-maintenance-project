# 🛠 Predictive Maintenance Dashboard (Streamlit)

This interactive dashboard allows users to input real-time machine data and get instant predictions on whether a tool failure is likely to occur. The model is trained using XGBoost and wrapped inside a preprocessing pipeline for production readiness.

---

## 🚀 Features

- 📊 Real-time prediction using a trained ML pipeline
- 🎛️ Interactive UI with sliders and dropdowns
- 📈 Display of classification performance (Confusion Matrix & Classification Report)
- 📦 Uses a serialized model pipeline (`xgb_pipeline_model.pkl`)
- Built with **Streamlit**

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

## 📦 How to Run the Dashboard Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/predictive-maintenance.git
   cd predictive-maintenance/dashboard
Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies

```bash
pip install -r requirements.txt
```
Run the app

```bash
streamlit run app.py
```
🗂 Folder Structure
```text
dashboard/
│
├── app.py                     # Streamlit app
├── xgb_pipeline_model.pkl     # Trained pipeline model
├── requirements.txt           # Streamlit + ML libraries
└── README.md                  # You're here!
```
📊 Example Output
✅ Prediction: Failure / No Failure

🧾 Confusion Matrix

🧾 Classification Report (Precision, Recall, F1-score)

⚙️ Notes
Ensure the model pipeline includes all preprocessing (like Label Encoding).

Input feature names in your app must match what the model expects.

The prediction results are based on a binary classification:

1: Failure

0: No Failure

🧠 Model Info
Model Used: XGBoost Classifier

Performance:

Accuracy: ~98%

Recall for Failures: ~81%

F1-Score for Failures: ~72%

Problem Type: Binary Classification

👩‍💻 Author
Durdana Khalid
Data Science Portfolio Project
GitHub: @DurdanaKhalid49

📜 License
Distributed under the MIT License. See LICENSE in the root directory for more information.
