import pytest
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

@pytest.fixture
def model():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemini-2.0-flash-lite")

def ask_gemini(model, prompt):
    """Helper: send a prompt to Gemini, return the text response."""
    time.sleep(3)  # wait 3 seconds between each API call
    response = model.generate_content(prompt)
    return response.text