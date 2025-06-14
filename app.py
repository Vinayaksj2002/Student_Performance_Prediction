import streamlit as st
import numpy as np
import joblib
from PIL import Image
import home, predict, about, dash,paragraph

# Load trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')


# Streamlit UI
st.title("📊 Student Performance Prediction")
st.image("StdStudent.gif")



# Initialize session state for page tracking
if "page" not in st.session_state:
    st.session_state.page = "paragraph"  # Default page

# Sidebar Navigation
with st.sidebar:
    st.title("📌 Menu")
    st.image("studentperformance.gif")
    if st.button("🏠 Home"):
        st.session_state.page = "home"
    if st.button("📊 Predict"):
        st.session_state.page = "predict"
    if st.button("📈Performance Panel"):
        st.session_state.page = 'dash'
    if st.button("ℹ️ About"):
        st.session_state.page = "about"



# Show selected page
if st.session_state.page == "home":
    home.show_home()
if st.session_state.page == "predict":
    predict.show_predict()
if st.session_state.page == "dash":
    dash.show_dash()
if st.session_state.page == "about":
    about.show_about()

if st.session_state.page == "paragraph":  # Paragraph page will load by default
    paragraph.show_paragraph() 

