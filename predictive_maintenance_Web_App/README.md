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
