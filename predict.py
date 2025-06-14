import streamlit as st

def show_predict():
        # Create a two-column layout
    col1, col2 = st.columns([1, 2])  # Left (Image) | Right (Content)

    with col1:
        # Add an image on the left
        st.image("prediction.gif", use_container_width=500)  # Replace with your image path

    with col2:
        st.title("📊Prediction")
    st.markdown("### For Example , How Does This App Predict !")
    st.markdown("## Enter student details below to predict their academic performance. ")

    # Collect user inputs
    study_time = st.slider("📖 Study Time (Hours per Day)", 1, 10, 3)
    past_grades = st.slider("📊 Previous Grades (out of 100)", 0, 100, 75)
    attendance = st.slider("📅 Attendance (%)", 0, 100, 90)
    parental_education = st.selectbox("🎓 Parental Education Level", ["No Degree", "High School", "Bachelor's", "Master's", "PhD"])
    
    # Process Prediction (Dummy Logic for Now)
    if st.button("🔮 Predict Performance"):
        if past_grades > 80 and study_time > 5:
            st.success("✅ Prediction: Excellent Performance! 🚀")
        elif past_grades > 60:
            st.info("⚠️ Prediction: Good, but Can Improve!")
        else:
            st.warning("❌ Prediction: Needs More Effort! 📚")

    # Button to go back to Home
    if st.button("🏠 Go to Home"):
        st.session_state.page = "home"
        st.rerun()
