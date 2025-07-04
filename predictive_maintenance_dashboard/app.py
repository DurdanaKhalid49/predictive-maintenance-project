# app.py

import streamlit as st
import pandas as pd
from utils.helper import load_model, plot_confusion_matrix, get_classification_report

st.set_page_config(page_title="Predictive Maintenance", layout="centered")
st.title("🔧 Predictive Maintenance Dashboard")

# Load Model
model = load_model("predictive_maintenance_dashboard/model/xgb_pipeline_model.joblib")

st.sidebar.header("Enter Input Features")

# User Inputs
type_input = st.sidebar.selectbox("Type", options=["L", "M", "H"])  
air_temp = st.sidebar.number_input("Air temperature [K]", value=300.0, step=1.0)
process_temp = st.sidebar.number_input("Process temperature [K]", value=310.0, step=1.0)
rot_speed = st.sidebar.number_input("Rotational speed [rpm]", value=1500, step=1)
torque = st.sidebar.number_input("Torque [Nm]", value=40.0, step=1.0)
tool_wear = st.sidebar.number_input("Tool wear [min]", value=10, step=1)

input_dict = {
    "Type": type_input,
    "Air temperature [K]": air_temp,
    "Process temperature [K]": process_temp,
    "Rotational speed [rpm]": rot_speed,
    "Torque [Nm]": torque,
    "Tool wear [min]": tool_wear,
}

input_df = pd.DataFrame([input_dict])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    pred_proba = model.predict_proba(input_df)[0]

    st.success(f"🔍 Prediction: {'Failure' if prediction == 1 else 'No Failure'}")
    st.write(f"Confidence: {max(pred_proba):.2%}")

# Optionally show evaluation (on test data)
st.markdown("---")
st.subheader("📊 Model Performance (Test Set)")

if st.checkbox("Show Confusion Matrix and Classification Report"):
    # Load your saved test set here if available
    try:
        test_data = pd.read_csv("data/predictive_maintenance.csv")  # Optional, if you saved X_test, y_test
        X_test = test_data.drop(columns=["Target"])
        y_test = test_data["Target"]
        y_pred = model.predict(X_test)

        # Confusion Matrix
        st.pyplot(plot_confusion_matrix(y_test, y_pred))

        # Classification Report
        st.dataframe(get_classification_report(y_test, y_pred))

    except FileNotFoundError:
        st.warning("❌ Test data not found. Upload it or remove the section.")
