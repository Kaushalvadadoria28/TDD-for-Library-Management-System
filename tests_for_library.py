import unittest
from library import Library,Book

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

if __name__ == "__main__":
    unittest.main()