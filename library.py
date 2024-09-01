class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class BookNotFoundError(Exception):
    """Exception raised when a book is not found in the library."""
    pass

class BookUnavailableError(Exception):
    """Exception raised when a book is not available for borrowing."""
    pass

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance")
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    def borrow_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        if not book.available:
            raise BookUnavailableError(f"The book '{book.title}' is currently unavailable.")
        book.available = False

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            raise BookNotFoundError(f"No book found with ISBN {isbn}.")
        book.available = True

    def view_available_books(self):
        return [book for book in self.books.values() if book.available]