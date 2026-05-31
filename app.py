import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Initialize Gemini
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

st.title("AI Image Analyzer")

# 1. Initialize result in session state to survive reruns
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # 2. When button is clicked, save the result to session_state
    if st.button("Analyze Image"):
        st.write("Analyzing...")
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(["Describe this image in detail", image])
            st.session_state.analysis_result = response.text
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 3. Always check if a result exists in memory and display it
if st.session_state.analysis_result:
    st.subheader("Gemini's Analysis Report:")
    st.write(st.session_state.analysis_result)
