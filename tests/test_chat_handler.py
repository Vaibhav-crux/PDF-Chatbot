# tests/test_chat_handler.py
import unittest
from unittest.mock import patch
from app.chat.chat_handler import handle_userinput

class TestChatHandler(unittest.TestCase):

    @patch('app.chat_handler.fetch_pdf_text', return_value="Mock PDF text")
    @patch('app.chat_handler.genai.GenerativeModel.generate_content')
    def test_handle_userinput(self, mock_generate_content, mock_fetch_pdf_text):
        mock_generate_content.return_value = type('obj', (object,), {'text': "Mock response"})
        response = handle_userinput("What is this PDF about?")
        self.assertEqual(response, "Mock response")

if __name__ == '__main__':
    unittest.main()
