class Library:
    def __init__(self):
        # Probably change inventory into a dict to make lookups easier
        self.inventory = []
        self.borrowers = {}
    
    def add_book(self, book):
        self.inventory.append(book)

    def add_borrower(self, borrower):
        self.borrowers[borrower.name] = borrower

    def find_borrower(self, name):
        return self.borrowers.get(name)
    
    def find_book(self, title):
        for book in self.inventory:
            if book.title == title:
                return book
        return None
    
    def checkout_book(self, book, borrower):
        if book in self.inventory and book.available:
            book.availble = False
            borrower.borrowed_books.append(book)
        else:
            print(book.title + " is not available.")

    def return_book(self, book, borrower):
        if book in borrower.borrowed_books:
            book.available = True
            borrower.borrowed_books.remove(book)
        else:
            print(borrower.name + " didn't borrow " + book.title + ".")

    def list_inventory(self):
        return [book.title for book in self.inventory if book.available]
    
    def list_borrowers(self):
        return list(self.borrowers.keys())