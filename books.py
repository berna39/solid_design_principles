class Books:
    def __init__(self):
        self.books = {}
        self.number = 0
    
    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book
    
    def __str__(self):
        return f'books i have read : ' + str(self.books)

class StoreBooks:
    @staticmethod
    def store_books(filename, books):
        with open(filename, 'w') as f:
            f.write(str(books))



b = Books()
b.add_book('Clean code')
b.add_book('Atomic habits')
print(b)

storage = StoreBooks()
storage.store_books('my_books.txt', b.books)


    
