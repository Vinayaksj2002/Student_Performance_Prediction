import streamlit as st

def show_home():
    # Create a two-column layout
    col1, col2 = st.columns([1, 2])  # Left (Image) | Right (Content)

    with col1:
        # Add an image on the left
        st.image("How_to_use.gif", use_container_width=500)  # Replace with your image path

    with col2:
        st.markdown("### 🔍 How to Use:")
        st.markdown("""
        1. Navigate to the **Predict** page.
        2. Enter student details.
        3. Get performance predictions instantly.
        """)

        st.markdown("### 🚀 Features:")
        st.markdown("""
        - **Make Predictions**: Get insights into student performance.
        - **User-Friendly Interface**: Easy to navigate and use.
        - **Real-time Processing**: Instant predictions based on inputs.
        """)

    # Optional: Home button to refresh the page
    if st.button("🔄 Refresh Home"):
        st.rerun()
