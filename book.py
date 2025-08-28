from app import get_connection

class Book:
    @staticmethod
    def add(title, author, genre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
                       (title, author, genre))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books
