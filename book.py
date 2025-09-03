from database import SessionLocal
from models import Book

class BookService:
    @staticmethod
    def add(title, author, genre):
        session = SessionLocal()
        book = Book(title=title, author=author, genre=genre)
        session.add(book)
        session.commit()
        session.refresh(book)
        session.close()
        return book

    @staticmethod
    def all():
        session = SessionLocal()
        books = session.query(Book).all()
        session.close()
        return books
