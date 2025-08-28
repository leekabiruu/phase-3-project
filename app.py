import sqlite3

DB_NAME = "library.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        book_id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT,
                        available INTEGER DEFAULT 1
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                        member_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        transaction_id INTEGER PRIMARY KEY,
                        book_id INTEGER,
                        member_id INTEGER,
                        issue_date TEXT,
                        return_date TEXT,
                        FOREIGN KEY (book_id) REFERENCES books(book_id),
                        FOREIGN KEY (member_id) REFERENCES members(member_id)
                    )''')

    conn.commit()
    conn.close()
