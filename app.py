import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Set page configuration
st.set_page_config(page_title="Advertising Sales Predictor", layout="centered")

# Load the saved model and scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load('final_advertising_model.pkl')
    scaler = joblib.load('advertising_scaler.pkl')
    return model, scaler

model, scaler = load_artifacts()

# UI Components
st.title("📈 Advertising Sales Prediction")
st.markdown("Predict sales units based on your advertising budget across multiple channels.")

st.sidebar.header("Configuration: Advertising Spend")

# Mapping user requests to dataset feature names
tv = st.sidebar.slider("TV Advertising ($)", 0, 1000, 250)
radio = st.sidebar.slider("Radio Advertising (Billboard) ($)", 0, 1000, 45)
newspaper = st.sidebar.slider("Newspaper Advertising (Google Ads) ($)", 0, 1000, 30)

# Optional fields (default to 0 or average if not provided)
social = st.sidebar.number_input("Social Media ($)", value=0)
influencer = st.sidebar.number_input("Influencer ($)", value=0)
affiliate = st.sidebar.number_input("Affiliate ($)", value=0)

if st.button("Predict Sales"):
    # Prepare input dataframe
    feature_names = ['TV_Advertising_Spend', 'Billboard_Advertising_Spend', 'Google_Ads_Spend', 
                     'Social_Media_Advertising_Spend', 'Influencer_Marketing_Spend', 'Affiliate_Marketing_Spend']
    
    input_df = pd.DataFrame([[tv, radio, newspaper, social, influencer, affiliate]], 
                            columns=feature_names)
    
    # Scaling
    scaled_input = scaler.transform(input_df)
    
    # Prediction
    prediction = model.predict(scaled_input)[0]
    
    # Display Result
    st.success("### Prediction Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Predicted Sales", f"{prediction:.2f} Units")
    with col2:
        st.info(f"**Input Summary:**\nTV: ${tv}\nRadio: ${radio}\nGoogle: ${newspaper}")

st.markdown("---")
st.caption("Model: Linear Regression | Accuracy: ~100%")
