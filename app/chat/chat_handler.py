# app/chat_handler.py
import google.generativeai as genai
from config.config import GOOGLE_API_KEY
from models.database import fetch_pdf_text

genai.configure(api_key=GOOGLE_API_KEY)

def handle_userinput(user_question):
    # Query the SQLite database for relevant text
    pdf_text = fetch_pdf_text()
    
    # Use the relevant text along with the user's question to generate a response
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(f"You are a bot. User: {user_question}. PDF Text: {pdf_text}")
    return response.text.strip()
