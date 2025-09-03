from database import SessionLocal
from models import Transaction, Book, Member
from datetime import datetime

class LoanService:
    @staticmethod
    def borrow(book_id, member_id, issue_date):
        session = SessionLocal()
        book = session.query(Book).filter_by(book_id=book_id).first()
        member = session.query(Member).filter_by(member_id=member_id).first()

        if not book:
            print("Book not found.")
        elif not member:
            print("Member not found.")
        elif not book.available:
            print("Book not available.")
        else:
            loan = Transaction(
                book_id=book_id,
                member_id=member_id,
                issue_date=datetime.fromisoformat(issue_date)
            )
            book.available = False
            session.add(loan)
            session.commit()
            print("Book borrowed successfully.")

        session.close()

    @staticmethod
    def return_book(book_id, return_date):
        session = SessionLocal()
        loan = session.query(Transaction).filter(
            Transaction.book_id == book_id,
            Transaction.return_date.is_(None)
        ).first()

        if loan:
            loan.return_date = datetime.fromisoformat(return_date)
            loan.book.available = True
            session.commit()
            print("Book returned successfully.")
        else:
            print("No active loan found for this book.")

        session.close()

    @staticmethod
    def borrowed_by(member_id):
        session = SessionLocal()
        loans = session.query(Transaction).filter(
            Transaction.member_id == member_id,
            Transaction.return_date.is_(None)
        ).all()
        session.close()
        return loans
