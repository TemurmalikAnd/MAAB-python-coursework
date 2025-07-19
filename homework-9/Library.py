class BookNotFoundException(Exception):
    def __init__(self, message="Book not found in library."):
        super().__init__(message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message="Book is already borrowed."):
        super().__init__(message)

class MemberLimitExceededException(Exception):
    def __init__(self, message="Member has reached the maximum borrow limit (3 books)."):
        super().__init__(message)


class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self, books_file="books.txt", members_file="members.txt"):
        self.books_file = books_file
        self.members_file = members_file

    def add_book(self, title, author):
        with open(self.books_file, 'a') as f:
            f.write(f"{title} | {author} | Available\n")
        print(f"Book '{title}' by {author} added.")

    def add_member(self, name):
        with open(self.members_file, 'a') as f:
            f.write(f"{name}\n")
        print(f"Member '{name}' added.")

    def borrow_book(self):
        member_name = input("Enter member name: ").strip()
        book_title = input("Enter book title to borrow: ").strip()

        # Load members
        with open(self.members_file, 'r') as f:
            members = [line.strip().split(" | ") for line in f.readlines()]

        # Check member
        member_found = False
        for m in members:
            if m[0] == member_name:
                member_found = True
                if len(m) - 1 >= 3:
                    raise MemberLimitExceededException()
                break
        if not member_found:
            raise Exception("Member not found.")

        # Load books
        with open(self.books_file, 'r') as f:
            books = [line.strip().split(" | ") for line in f.readlines()]

        book_found = False
        updated_books = []
        for b in books:
            if b[0] == book_title:
                book_found = True
                if b[2].strip().lower() != "available":
                    raise BookAlreadyBorrowedException()
                b[2] = "Not available"
            updated_books.append(" | ".join(b) + "\n")

        if not book_found:
            raise BookNotFoundException()

        # Save updated books
        with open(self.books_file, 'w') as f:
            f.writelines(updated_books)

        # Update members
        updated_members = []
        for m in members:
            if m[0] == member_name:
                m.append(book_title)
            updated_members.append(" | ".join(m) + "\n")
        with open(self.members_file, 'w') as f:
            f.writelines(updated_members)

        print(f"{member_name} successfully borrowed '{book_title}'.")

    def return_book(self):
        member_name = input("Enter member name: ").strip()
        book_title = input("Enter book title to return: ").strip()

        # Update books
        with open(self.books_file, 'r') as f:
            books = [line.strip().split(" | ") for line in f.readlines()]
        updated_books = []
        found = False
        for b in books:
            if b[0] == book_title:
                b[2] = "Available"
                found = True
            updated_books.append(" | ".join(b) + "\n")
        if not found:
            raise BookNotFoundException()
        with open(self.books_file, 'w') as f:
            f.writelines(updated_books)

        # Update members
        with open(self.members_file, 'r') as f:
            members = [line.strip().split(" | ") for line in f.readlines()]
        updated_members = []
        for m in members:
            if m[0] == member_name:
                if book_title in m:
                    m.remove(book_title)
            updated_members.append(" | ".join(m) + "\n")
        with open(self.members_file, 'w') as f:
            f.writelines(updated_members)

        print(f"{member_name} successfully returned '{book_title}'.")

    def show_all_books(self):
        print("\nBooks in Library:")
        with open(self.books_file, 'r') as f:
            for line in f:
                print(line.strip())

    def show_all_members(self):
        print("\nMembers:")
        with open(self.members_file, 'r') as f:
            for line in f:
                print(line.strip())

    def main_menu(self):
        while True:
            print("\n===== Library Management Menu =====")
            print("1. Add a Book")
            print("2. Add a Member")
            print("3. Borrow a Book")
            print("4. Return a Book")
            print("5. Show All Books")
            print("6. Show All Members")
            print("0. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    self.add_book(title, author)
                elif choice == 2:
                    name = input("Enter member name: ")
                    self.add_member(name)
                elif choice == 3:
                    self.borrow_book()
                elif choice == 4:
                    self.return_book()
                elif choice == 5:
                    self.show_all_books()
                elif choice == 6:
                    self.show_all_members()
                elif choice == 0:
                    print("Exiting Library System. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a number.")
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    library = Library()
    library.main_menu()
