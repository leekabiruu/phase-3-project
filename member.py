from app import get_connection

class Member:
    @staticmethod
    def add(name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        conn.close()
        return members
