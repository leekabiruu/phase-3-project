import cmd
from book import BookService
from member import MemberService
from loan import LoanService

class LibraryCLI(cmd.Cmd):
    intro = "Welcome to the library system. Type help or ? to list commands."
    prompt = "(library) "

    def do_add_book(self, arg):
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        book = BookService.add(title, author, genre)
        print(f"Book added: {book.title} by {book.author}")

    def do_view_books(self, arg):
        books = BookService.all()
        for b in books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.book_id}: {b.title} by {b.author} ({b.genre}) - {status}")

    def do_add_member(self, arg):
        name = input("Name: ")
        email = input("Email: ")
        member = MemberService.add(name, email)
        print(f"Member added: {member.name} ({member.email})")

    def do_view_members(self, arg):
        members = MemberService.all()
        for m in members:
            print(f"{m.member_id}: {m.name} ({m.email})")

    def do_borrow(self, arg):
        book_id = int(input("Book ID: "))
        member_id = int(input("Member ID: "))
        issue_date = input("Issue Date (YYYY-MM-DD): ")
        LoanService.borrow(book_id, member_id, issue_date)

    def do_return(self, arg):
        book_id = int(input("Book ID: "))
        return_date = input("Return Date (YYYY-MM-DD): ")
        LoanService.return_book(book_id, return_date)

    def do_view_borrowed(self, arg):
        member_id = int(input("Member ID: "))
        loans = LoanService.borrowed_by(member_id)
        if not loans:
            print("No borrowed books.")
        else:
            for loan in loans:
                print(f"{loan.book.title} by {loan.book.author} (Issued: {loan.issue_date.date()})")

    def do_exit(self, arg):
        print("Goodbye!")
        return True
