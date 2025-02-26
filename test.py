
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API
genai.configure(api_key=API_KEY)

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
