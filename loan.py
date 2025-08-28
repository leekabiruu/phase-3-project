from app import get_connection

class Loan:
    @staticmethod
    def borrow(book_id, member_id, issue_date):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT available FROM books WHERE book_id=?", (book_id,))
        book = cursor.fetchone()
        if not book or book[0] == 0:
            print("Book not available.")
        else:
            cursor.execute("INSERT INTO transactions (book_id, member_id, issue_date) VALUES (?, ?, ?)",
                           (book_id, member_id, issue_date))
            cursor.execute("UPDATE books SET available=0 WHERE book_id=?", (book_id,))
            conn.commit()
            print("Book borrowed successfully.")

        conn.close()

    @staticmethod
    def return_book(book_id, return_date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE transactions SET return_date=? WHERE book_id=? AND return_date IS NULL",
                       (return_date, book_id))
        cursor.execute("UPDATE books SET available=1 WHERE book_id=?", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def borrowed_by(member_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT b.title, b.author, t.issue_date 
                          FROM transactions t
                          JOIN books b ON b.book_id = t.book_id
                          WHERE t.member_id=? AND t.return_date IS NULL''',
                       (member_id,))
        books = cursor.fetchall()
        conn.close()
        return books
