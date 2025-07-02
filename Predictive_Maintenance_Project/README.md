# 🛠 Predictive Maintenance - ML Web App

This project is a machine learning-powered web app that predicts equipment failure based on input conditions using a trained XGBoost pipeline. 

🚀 Built with:
- **Flask**: for the web app interface
- **Streamlit**: for the interactive dashboard
- **XGBoost**: for classification
- **Scikit-learn Pipelines**: for clean preprocessing and prediction

---

## 🔍 Use Case

Predictive maintenance helps reduce downtime by forecasting failures before they occur. This model uses:
- Type of equipment
- Air and process temperature
- Rotational speed
- Torque
- Tool wear

---

## 📁 Project Structure
```
predictive-maintenance-project/
├── predictive_maintenance_Web_App # Flask app
  ├── app.py
  ├── templates/
    ├── index.html
  ├── model/
    │ └── xgb_pipeline_model.pkl
  ├── requirement.txt
  ├── README.md
  ├── Procfile
├── predictive_maintenance_dashboard # Streamlit dashboard
  ├── app.py
  ├── utils/
    ├── helper.py
  ├── model/
    │ └── xgb_pipeline_model.pkl
  ├── requirement.txt
  ├── README.md
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```



## 🚦 How to Run Locally

### 🧪 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```
🌐 3. Run Flask App
```bash
python app.py
Visit http://localhost:5000
```
📊 4. Run Streamlit Dashboard
```bash 
streamlit run streamlit_app.py
```
🌍 Deployment
Flask: deployed on Render

Streamlit: deployed on Streamlit Cloud

👤 Author
Durdana Khalid
Data Scientist | ML Enthusiast | Freelancer
🌐 LinkedIn | 📫 durdanakhalid98@gmail.com
