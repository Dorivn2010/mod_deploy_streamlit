import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder



#load the model
model = pickle.load(open('Rf_Model.sav','rb'))

# Define the categorical features and their possible values
categorical_features = {
    'gender': ['Female', 'Male'],
    'Partner': ['No', 'Yes'],
    'Dependents': ['No', 'Yes'],
    'PhoneService': ['No', 'Yes'],
    'MultipleLines': ['No phone service', 'No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No internet service', 'No', 'Yes'],
    'OnlineBackup': ['No internet service', 'No', 'Yes'],
    'DeviceProtection': ['No internet service', 'No', 'Yes'],
    'TechSupport': ['No internet service', 'No', 'Yes'],
    'StreamingTV': ['No internet service', 'No', 'Yes'],
    'StreamingMovies': ['No internet service', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['No', 'Yes'],
    'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
}

#Define encoder dictionary 
encoder_dict = {feature:LabelEncoder().fit(choices) for feature,choices in categorical_features.items()}

#streamlit app
st.set_page_config(page_title='Customer Churn Prediction',page_icon=":bar_chart:",layout="centered",initial_sidebar_state="expanded")