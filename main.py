from library import Library
from borrower import Borrower
from book import Book

# Create Books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")
book4 = Book("Pride and Prejudice", "Jane Austen")

# Add books to Library
lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

def main():
    while True:
        print("Choose an option:")
        print("1. Add a new book to inventory")
        print("2. Checkout a book for a borrower")
        print("3. Return a book for a borrower")
        print("4. List the available books")
        print("Type 'exit' to exit the application")

        choice = input("Enter the number of your choice: ")
        print("\n")

        if choice == '1':
            continue
        elif choice == '2':
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            print(lib.list_inventory())
        elif choice == 'exit':
            break
        else:
            print(f"{choice} is not a valid option")

if __name__ == "__main__":
    main()