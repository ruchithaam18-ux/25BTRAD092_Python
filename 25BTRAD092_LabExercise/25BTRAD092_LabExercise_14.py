
# LAB EXERCISE 14: LIBRARY MANAGEMENT SYSTEM

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def display(self):
        status = "Available" if self.available_copies > 0 else "Issued"
        print(
            f"{self.book_id:<10}{self.title[:24]:<25}"
            f"{self.author[:19]:<20}"
            f"{self.available_copies:>8}"
            f"{status:>14}"
        )


# Inheritance: Library inherits from Book
class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()

        if not book_id or book_id in self.books:
            print("Invalid or duplicate Book ID!")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        if not title or not author:
            print("Title and author cannot be empty!")
            return

        try:
            copies = int(input("Enter Number of Copies: "))
            if copies <= 0:
                print("Copies must be greater than zero!")
                return
        except ValueError:
            print("Invalid number of copies!")
            return

        self.books[book_id] = Book(
            book_id, title, author, copies
        )
        print("Book added successfully!")

    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ").strip()

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book.available_copies == 0:
            print("Book unavailable! All copies are issued.")
            return

        student = input("Enter Student Name: ").strip()

        if not student:
            print("Student name cannot be empty!")
            return

        key = (book_id, student.lower())

        if key in self.issued:
            print("This student already has this book!")
            return

        book.available_copies -= 1
        self.issued[key] = student

        print(f"Book '{book.title}' issued to {student}!")

    def return_book(self):
        book_id = input("Enter Book ID to Return: ").strip()
        student = input("Enter Student Name: ").strip()

        key = (book_id, student.lower())

        if key not in self.issued:
            print("No matching issue record found!")
            return

        book = self.books[book_id]
        book.available_copies += 1
        del self.issued[key]

        print(f"Book '{book.title}' returned successfully!")

    def search_book(self):
        keyword = input("Enter Book Title or Author: ").lower()
        found = False

        print("\n" + "=" * 77)
        print(f"{'ID':<10}{'Book Title':<25}"
              f"{'Author':<20}{'Copies':>8}{'Status':>14}")
        print("-" * 77)

        for book in self.books.values():
            if (keyword in book.title.lower()
                    or keyword in book.author.lower()):
                book.display()
                found = True

        if not found:
            print("No matching books found!")

        print("=" * 77)

    def display_books(self):
        if not self.books:
            print("Library is empty!")
            return

        print("\n" + "=" * 77)
        print("LIBRARY BOOK INVENTORY".center(77))
        print("=" * 77)
        print(f"{'ID':<10}{'Book Title':<25}"
              f"{'Author':<20}{'Copies':>8}{'Status':>14}")
        print("-" * 77)

        for book in self.books.values():
            book.display()

        print("=" * 77)

    def display_issued(self):
        print("\n" + "=" * 60)
        print("ISSUED BOOK RECORDS".center(60))
        print("=" * 60)

        if not self.issued:
            print("No books are currently issued!")
        else:
            print(f"{'Book ID':<15}{'Book Title':<25}{'Student':<20}")
            print("-" * 60)

            for (book_id, _), student in self.issued.items():
                book = self.books[book_id]
                print(
                    f"{book_id:<15}"
                    f"{book.title[:24]:<25}"
                    f"{student[:19]:<20}"
                )

        print("=" * 60)


library = Library()

while True:
    print("\n" + "=" * 45)
    print("LIBRARY MANAGEMENT SYSTEM".center(45))
    print("=" * 45)
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. Display Issued Books")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.search_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        library.display_issued()
    elif choice == "7":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
