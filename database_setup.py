# database_setup.py
import sqlite3

def create_connection():
    return sqlite3.connect('finance_tracker.db')

def create_tables():
    conn = create_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category_id INTEGER,
            date TEXT,
            description TEXT
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY,
            goal REAL,
            achieved REAL DEFAULT 0
        )''')
    print("Database and tables created successfully.")
