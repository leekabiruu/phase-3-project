from app import init_db
from cli import LibraryCLI

if __name__ == "__main__":
    init_db()
    LibraryCLI().cmdloop()
