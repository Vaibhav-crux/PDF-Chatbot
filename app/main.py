# app/main.py
import streamlit as st
from services.pdf_processing import get_pdf_text
from models.database import save_to_database
from chat.chat_handler import handle_userinput

def main():
    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")
    
    # Load CSS
    with open("app/static/styles.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
    
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
