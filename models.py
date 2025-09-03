from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    available = Column(Boolean, default=True)

    transactions = relationship("Transaction", back_populates="book")

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    transactions = relationship("Transaction", back_populates="member")

    def __repr__(self):
        return self.name

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    member_id = Column(Integer, ForeignKey("members.member_id"))
    issue_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime)

    book = relationship("Book", back_populates="transactions")
    member = relationship("Member", back_populates="transactions")

    def __repr__(self):
        return f"Loan: {self.book_id} -> {self.member_id}"
