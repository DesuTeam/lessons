import unittest
from Book import Book
from Customer import Customer
from Library import Library
from LogicException import LogicException


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()



    def test_can_add_book(self):
        self.library.add_book(Book(1, 'byte_of_python', 'programmer', 2009))

        book = self.library.get_book_by_id(1)

        self.assertEqual(1, book.id)
        self.assertEqual('byte_of_python', book.name)
        self.assertEqual('programmer', book.author)
        self.assertEqual(2009, book.year)

    def test_can_t_get_nonexisting_book(self):
        with self.assertRaises(LogicException):
            self.library.get_book_by_id(1)

    def test_can_t_delete_nonexisting_book(self):
        with self.assertRaises(LogicException):
            self.library.del_book(1)

    def test_delete_book(self):
        book = Book(0, 'Death', 'None', 2005)
        self.library.add_book(book)

        self.library.del_book(0)

        self.assertEqual([], self.library.get_books())

    def test_no_books_by_default(self):
        self.assertEqual([], self.library.get_books())

    def test_add_book(self):
        book = Book(0, 'Death', 'None', 2005)
        self.library.add_book(book)

        books = self.library.get_books()

        self.assertEqual([book], books)

    def test_no_customers_by_default(self):
        self.assertEqual(0, self.library.get_customers_count())

    def test_can_add_customer(self):
        customer = Customer(1, 'Becca')

        self.library.add_customer(customer)

        self.assertEqual(1, self.library.get_customers_count())

