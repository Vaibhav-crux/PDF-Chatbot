import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import sqlite3
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = "AIzaSyCvEsb6RYKpdeIMmeOlEP8Gn910H5BocsY"

genai.configure(api_key=GOOGLE_API_KEY)

# Function to read text from PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to save text into SQLite database
def save_to_database(text):
    conn = sqlite3.connect('pdf_text.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pdf_text (id INTEGER PRIMARY KEY, text TEXT)''')
    # Delete existing data
    c.execute("DELETE FROM pdf_text")
    # Insert new text
    c.execute("INSERT INTO pdf_text (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

# Function to handle user input using Gemini API
def handle_userinput(user_question):
    # Query the SQLite database for relevant text
    conn = sqlite3.connect('pdf_text.db')
    c = conn.cursor()
    c.execute("SELECT text FROM pdf_text")
    pdf_text = c.fetchone()[0]
    conn.close()
    
    # Use the relevant text along with the user's question to generate a response
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(f"You are a bot. User: {user_question}. PDF Text: {pdf_text}")
    return response.text.strip()

def main():
    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")
    # Load CSS
    css = """
    CSS styles here
    """
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    st.header("Chat with PDF :books:")
    user_question = st.text_input("Ask a question about your document:")
    if user_question:
        response = handle_userinput(user_question)
        st.write(response)
    with st.sidebar:
        st.subheader("Your document")
        pdf_doc = st.file_uploader("Upload your PDF here and click on 'Process'", type=['pdf'])
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get pdf text
                raw_text = get_pdf_text([pdf_doc])
                # Save to database
                save_to_database(raw_text)
                # Show processing status in the UI
                st.success("PDF text has been processed and saved.")

if __name__ == '__main__':
    main()
