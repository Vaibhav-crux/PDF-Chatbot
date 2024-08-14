# tests/test_database.py
import unittest
import sqlite3
from app.models.database import save_to_database, fetch_pdf_text

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_path = 'test_pdf_text.db'

    def tearDown(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS pdf_text")
        conn.commit()
        conn.close()

    def test_save_and_fetch_pdf_text(self):
        save_to_database("Test PDF text", self.db_path)
        text = fetch_pdf_text(self.db_path)
        self.assertEqual(text, "Test PDF text")

if __name__ == '__main__':
    unittest.main()
