import streamlit as st

def show_about():
          # Create a two-column layout
    col1, col2 = st.columns([1, 1])  # Left (Image) | Right (Content)
    with col1:
     st.title("ℹ️ About the App")
    
    st.markdown("""
    ## 🎯 Purpose of This App  
    This **Student Performance Prediction App** helps educators, students, and parents understand and analyze student progress using **Machine Learning**.
    
    ## 📈 How It Works:
    - Users input details like **study time, attendance, past grades, and parental education**.
    - The app predicts student performance based on historical data patterns.
    - The results provide insights to **improve academic success**.

    ## 🤖 Technologies Used:
    - **Python & Streamlit**: For building the web app.
    - **Pandas & NumPy**: For data processing.
    - **Machine Learning**: (Future) Could integrate scikit-learn for actual predictions.

    ## 👨‍🏫 Who Can Use This App?
    - **Students** 📚: To assess their learning habits.
    - **Teachers** 🍎: To identify students who need support.
    - **Parents** 🏡: To track their child's academic progress.

    🎯 Our goal is to help students **succeed academically!** 🚀
    
    ## 👨‍💻 Developed By
    *streamlit run app.pyVinayak Sanjay Jadhav*  
    📧 `vinayaksjadhav2002@gmail.com`  
    [GitHub – Vinayaksj2002](https://github.com/Vinayaksj2002)
    """)
    # Button to go back to Home
    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()
