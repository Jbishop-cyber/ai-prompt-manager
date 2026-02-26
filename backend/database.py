import sqlite3
import os  # <-- new import

def create_connection():
    # Get the folder of this script (backend/)
    current_dir = os.path.dirname(__file__)
    # Build the path to the data folder
    db_path = os.path.join(current_dir, '../data/prompts.db')
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT,
            prompt_text TEXT NOT NULL,
            example_output TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database and table created successfully.")