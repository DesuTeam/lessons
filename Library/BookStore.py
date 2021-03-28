from Library import Book
from LogicException import LogicException

class BookStore:
    def __init__(self):
        self.books = []

    def add(self, book: Book):
        self.books.append(book)

    def delete(self, id: int):
        self.has_or_fail(id)
        self.books = list(filter(lambda book: book.id != id, self.books))


    def get_by_id(self, id: int) -> Book:
        self.has_or_fail(id)
        for book in self.books:
            if id == book.id:
                return book

    def has_or_fail(self, book_id: int):
        if len(list(filter(lambda book: book.id == book_id, self.books))) == 0:
            raise LogicException('book with id: ' + str(id) + ' don\'t exist')

    def get_all(self):
        return self.books
