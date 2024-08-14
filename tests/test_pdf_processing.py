# tests/test_pdf_processing.py
import unittest
from app.services.pdf_processing import get_pdf_text

class TestPDFProcessing(unittest.TestCase):

    def test_get_pdf_text(self):
        # Test with a mock PDF file (can use PyPDF2 mock)
        pdf_docs = ["mock_pdf_1.pdf", "mock_pdf_2.pdf"]
        text = get_pdf_text(pdf_docs)
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()
