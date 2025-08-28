import cmd
from book import Book
from member import Member
from loan import Loan

class LibraryCLI(cmd.Cmd):
    intro = "Welcome to the library system. Type help or ? to list commands."
    prompt = "(library) "

    def do_add_book(self, arg):
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        Book.add(title, author, genre)
        print("Book added.")

    def do_view_books(self, arg):
        books = Book.all()
        for b in books:
            print(f"{b[0]}: {b[1]} by {b[2]} ({b[3]}) - {'Available' if b[4] else 'Borrowed'}")

    def do_add_member(self, arg):
        name = input("Name: ")
        email = input("Email: ")
        Member.add(name, email)
        print("Member added.")

    def do_view_members(self, arg):
        members = Member.all()
        for m in members:
            print(f"{m[0]}: {m[1]} ({m[2]})")

    def do_borrow(self, arg):
        book_id = int(input("Book ID: "))
        member_id = int(input("Member ID: "))
        issue_date = input("Issue Date (YYYY-MM-DD): ")
        Loan.borrow(book_id, member_id, issue_date)

    def do_return(self, arg):
        book_id = int(input("Book ID: "))
        return_date = input("Return Date (YYYY-MM-DD): ")
        Loan.return_book(book_id, return_date)

    def do_view_borrowed(self, arg):
        member_id = int(input("Member ID: "))
        books = Loan.borrowed_by(member_id)
        if not books:
            print("No borrowed books.")
        for b in books:
            print(f"{b[0]} by {b[1]} (Issued: {b[2]})")

    def do_exit(self, arg):
        print("Goodbye!")
        return True
