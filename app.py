import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

# Load environment variables (.env file)
load_dotenv()

# Initialize the Gemini Client
client = genai.Client()

def analyze_my_image():
    # Added your exact sidebar filename to the check list
    possible_names = ["test.jpg.jpg!.JPG", "test.jpg.jpg!", "test.jpg", "test"]
    image_filename = None

    # Check which file name actually exists in your folder
    for name in possible_names:
        if os.path.exists(name):
            image_filename = name
            break

    if image_filename is None:
        print("❌ Error: Could not find your picture in the folder!")
        print("Make sure your photo is inside 'ai-video-web' next to app.py.")
        return

    print(f"\n🚀 Found your image file: '{image_filename}'!")
    try:
        # Open your image safely
        img = Image.open(image_filename)
        
        # Use the free tier Gemini model to read it
        print("Analyzing your photo with Gemini... please wait...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[img, "Describe this image in deep detail and tell me exactly what you see."]
        )
        
        print("\n✨ --- GEMINI'S ANALYSIS REPORT --- ✨")
        print(response.text)
        print("---------------------------------------")
            
    except Exception as e:
        print(f"An error occurred while reading the image: {e}")

if __name__ == "__main__":
    analyze_my_image()