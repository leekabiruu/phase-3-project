from database import SessionLocal
from models import Member

class MemberService:
    @staticmethod
    def add(name, email):
        session = SessionLocal()
        member = Member(name=name, email=email)
        session.add(member)
        session.commit()
        session.refresh(member)
        session.close()
        return member

    @staticmethod
    def all():
        session = SessionLocal()
        members = session.query(Member).all()
        session.close()
        return members
