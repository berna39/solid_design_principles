from time import sleep


class Book:
    def __init__(self):
        self.books = {}
        self.number = 0
    
    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book
