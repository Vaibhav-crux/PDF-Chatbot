# Chat with PDF

## Overview

"Chat with PDF" is a web application that allows users to upload PDF documents, extract their text, and interact with the content through a chat interface. The application uses Streamlit for the frontend, a FastAPI-like approach for structuring the backend, and SQLite for storing extracted text. It also integrates with Google's Gemini API to generate responses based on the PDF content and user queries.

## Features

- **PDF Upload**: Upload and process PDF documents to extract text.
- **Text Storage**: Extracted text is stored in a SQLite database.
- **Chat Interface**: Ask questions about the uploaded PDF and get responses based on the content.
- **API Integration**: Uses Google’s Gemini API for generating AI-driven responses.

## Project Structure

```plaintext
pdf_chat/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── chat_handler.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── pdf_processing.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       └── layout.html
│
├── tests/
│   ├── __init__.py
│   ├── test_pdf_processing.py
│   ├── test_database.py
│   ├── test_chat_handler.py
│   └── test_main.py
│
├── .env
├── pdf_text.db
├── requirements.txt
└── README.md
```

## Installation

### Prerequisites

- Python 3.8+
- A Google API Key for the Gemini API

### Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/chat-with-pdf.git
    cd chat-with-pdf
    ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    - Create a `.env` file in the root directory and add your Google API key.

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

5. **Run the application**:

    ```bash
    streamlit run app/main.py
    ```

## Usage

- Open the Streamlit app in your web browser.
- Upload a PDF file using the sidebar.
- Once processed, ask questions related to the content of the PDF.
- The AI will generate responses based on the extracted text.

## Testing

To run tests for different modules:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request. 
