import unittest
from library import Library,Book,BookNotFoundError,BookUnavailableError

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book(isbn="1234567890", title="Python Programming", author="Kaushal vadadoria", publication_year=2015)
        self.book2 = Book(isbn="0987654321", title="Data Science 101", author="Kaushal vadadoria", publication_year=2017)

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn("1234567890", self.library.books)
        self.assertEqual(self.library.books["1234567890"], self.book1)

    def test_add_duplicate_book(self):
        self.library.add_book(self.book1)
        with self.assertRaises(ValueError):
            self.library.add_book(self.book1)

    def test_borrow_book(self):
        self.library.add_book(self.book1)
        self.library.borrow_book("1234567890")
        self.assertFalse(self.book1.available)

    def test_borrow_unavailable_book(self):
        self.library.add_book(self.book1)
        self.library.borrow_book("1234567890")
        with self.assertRaises(BookUnavailableError):
            self.library.borrow_book("1234567890")

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.borrow_book("9999999999")

    def test_return_book(self):
        self.library.add_book(self.book1)
        self.library.borrow_book("1234567890")
        self.library.return_book("1234567890")
        self.assertTrue(self.book1.available)

    def test_view_available_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.borrow_book("1234567890")
        available_books = self.library.view_available_books()
        self.assertIn(self.book2, available_books)
        self.assertNotIn(self.book1, available_books)

if __name__ == "__main__":
    unittest.main()