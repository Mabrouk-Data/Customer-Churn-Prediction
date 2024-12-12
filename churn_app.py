import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st
import joblib


def getInput():

    gender = st.selectbox("Select gender".title(), ["Male", "Female"])

    SeniorCitizen = st.selectbox("Are you a Senior Citizen ?".title(), [0, 1])

    Partner = st.selectbox("Do you have a partner ?".title(), ["Yes", "No"])

    Dependents = st.selectbox("Do you have any Dependents ?".title(), ["Yes", "No"])

    tenure = st.slider(
        "choose tenure (in months)".title(), min_value=0.0, max_value=72.0, step=3.0
    )

    PhoneService = st.selectbox("Do you have PhoneService ?".title(), ["Yes", "No"])

    MultipleLines = st.selectbox(
        "Do you have MultipleLines ?".title(), ["Yes", "No", "No phone service"]
    )

    InternetService = st.selectbox(
        "Select InternetService Type ?".title(), ["Fiber optic", "DSL", "No"]
    )

    OnlineSecurity = st.selectbox(
        "Do you have OnlineSecurity ?".title(), ["Yes", "No", "No internet service"]
    )

    OnlineBackup = st.selectbox(
        "Do you have OnlineBackup ?".title(), ["Yes", "No", "No internet service"]
    )

    DeviceProtection = st.selectbox(
        "Do you have DeviceProtection ?".title(), ["Yes", "No", "No internet service"]
    )

    TechSupport = st.selectbox(
        "Do you have TechSupport ?".title(), ["Yes", "No", "No internet service"]
    )

    StreamingTV = st.selectbox(
        "Do you have StreamingTV ?".title(), ["Yes", "No", "No internet service"]
    )

    StreamingMovies = st.selectbox(
        "Do you have StreamingMovies ?".title(), ["Yes", "No", "No internet service"]
    )

    Contract = st.selectbox(
        "Select Contract Type".title(), ["Month-to-month", "Two year", "One year"]
    )

    PaperlessBilling = st.selectbox(
        "Do you have PaperlessBilling ?".title(), ["Yes", "No"]
    )

    PaymentMethod = st.selectbox(
        "Select Payment Method".title(),
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)",
        ],
    )

    MonthlyCharges = st.slider(
        "Input your MonthlyCharges".title(), min_value=19.0, max_value=117.0, step=10.0
    )

    TotalCharges = st.slider(
        "Input your TotalCharges".title(), min_value=0.0, max_value=8680.0, step=100.0
    )

    return pd.DataFrame(
        data=[
            [
                gender,
                SeniorCitizen,
                Partner,
                Dependents,
                tenure,
                PhoneService,
                MultipleLines,
                InternetService,
                OnlineSecurity,
                OnlineBackup,
                DeviceProtection,
                TechSupport,
                StreamingTV,
                StreamingMovies,
                Contract,
                PaperlessBilling,
                PaymentMethod,
                MonthlyCharges,
                TotalCharges,
            ]
        ],
        columns=[
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges",
        ],
    )


test = getInput()
st.dataframe(test)
# model = joblib.load("model.h5")
model_path = (
    r"d:/Data Analyst/Final Project Customer Churn Project/churn proj code/churn_app.py"
)
model = joblib.load(model_path)

st.write(
    "Yes Customer Churns" if model.predict(test) == 1 else "No Customer Doesnt Churn"
)
