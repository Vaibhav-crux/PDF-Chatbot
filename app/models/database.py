import sqlite3

def save_to_database(text, db_path='pdf_text.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pdf_text (id INTEGER PRIMARY KEY, text TEXT)''')
    # Delete existing data
    c.execute("DELETE FROM pdf_text")
    # Insert new text
    c.execute("INSERT INTO pdf_text (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def fetch_pdf_text(db_path='pdf_text.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT text FROM pdf_text")
    pdf_text = c.fetchone()[0]
    conn.close()
    return pdf_text