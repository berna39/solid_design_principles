from time import sleep


class Books:
    def __init__(self):
        self.books = {}
        self.number = 0
    
    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book
    
    def __str__(self):
        return f'books i have read : ' + str(self.books)


b = Books()
b.add_book('Clean code')
b.add_book('Atomic habits')
print(b)

    
