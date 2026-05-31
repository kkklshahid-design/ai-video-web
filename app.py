import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables (.env file)
load_dotenv()

# Initialize the Gemini Client
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

import streamlit as st

st.title("AI Image Analyzer")

# Let the user upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Analyze button
    if st.button("Analyze Image"):
        st.write("Analyzing...")
        try:
            # Using the genai model initialized earlier
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(["Describe this image in detail", image])
            
            st.subheader("Gemini's Analysis Report:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
