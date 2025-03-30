import pytest
from book import Book

# Test valid book creation
@pytest.mark.parametrize("title, isbn", [
    ("Watchmen", "978-1779501127"),
    ("Clean Code", "9780132350884"),
    ("The Pragmatic Programmer", "9780201616224"),
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

# Test invalid title
@pytest.mark.parametrize("title, isbn", [
    ("", "978-1779501127"),  # Empty title
    ("   ", "9780132350884"),  # Whitespace-only title
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError, match="Title cannot be empty"):
        Book(title, isbn)

# Test invalid ISBN
@pytest.mark.parametrize("title, isbn", [
    ("Watchmen", "978-1779501128"),  # Invalid checksum
    ("Clean Code", "978013235088"),  # Less than 13 digits
    ("The Pragmatic Programmer", "97802016162245"),  # More than 13 digits
    ("Book Title", "978-ABC-1234567"),  # Non-numeric characters
    ("Another Book", "978-177950112"),  # Missing digits
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError, match="Invalid ISBN"):
        Book(title, isbn)