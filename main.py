from library import Library
from borrower import Borrower
from book import Book

import pickle

lib = Library()
FILENAME = 'library.pkl'

# Persistent Storage using Pickle
def load_library():
    try:
        with open(FILENAME, 'rb') as file:
            unpickler = pickle.Unpickler(file)
            return unpickler.load()
    except FileNotFoundError:
        return Library()

def save_library():
    try:
        with open(FILENAME, 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(lib)
    except pickle.PicklingError:
        print("Couldn't save library data")

def main():
    global lib
    lib = load_library()

    while True:
        print("Choose an option:")
        print("1. Add a new book")
        print("2. Add a new borrower")
        print("3. Checkout a book for a borrower")
        print("4. Return a book for a borrower")
        print("5. List the available books")
        print("Type 'exit' to exit the application\n")

        choice = input("Enter the number of your choice: ")
        print("\n")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            lib.add_book(book)
        elif choice == '2':
            name = input("Enter the name of the borrower")
            borrower = Borrower(name)
            lib.add_borrower(borrower)
        elif choice == '3':
            # Find the Book in the Inventory with a matching name
            # Find the Borrower with a matching name
            # Try to Checkout the book
            continue
        elif choice == '4':
            continue
        elif choice == '5':
            print(lib.list_inventory())
        elif choice == 'exit':
            save_library()
            break
        else:
            print(f"{choice} is not a valid option")

if __name__ == "__main__":
    main()