from dotenv import load_dotenv
import os
import google.generativeai as genai
from google import genai


def get_genai_client():
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    print(gemini_api_key)
    client = genai.Client(api_key=gemini_api_key)
    return client
