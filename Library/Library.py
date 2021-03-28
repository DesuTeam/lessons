from Book import Book
from Customer import Customer
from CustomerStore import CustomerStore
from BookStore import BookStore


class Library:
    def __init__(self):
        self.bookStore = BookStore()
        self.customerStore = CustomerStore()
        self.rentals = {}


    def add_customer(self, customer: Customer):
        self.customerStore.add(customer)

    def get_customers_count(self) -> int:
        return self.customerStore.count()

    def add_book(self, book: Book):
        self.bookStore.add(book)

    def del_book(self, id: int):
        self.bookStore.delete(id)

    def rent_book(self, book_id: int, customer_id: int):
        if not customer_id in self.rentals:
            self.rentals[customer_id] = []
        self.rentals[customer_id].append(book_id)


    def get_book_by_id(self, id: int) -> Book:
        return self.bookStore.get_by_id(id)

    def get_books(self):
        return self.bookStore.get_all()
