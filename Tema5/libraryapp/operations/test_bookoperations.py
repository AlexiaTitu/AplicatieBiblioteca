from libraryapp.domain.bookentity import get_id, get_titlu
from libraryapp.operations.bookoperations import delete_book, add_book

def test_add_book():
        all_books = []
        add_book(all_books, 1, "ceva", "fantasy", "Mihai Eminescu")
        assert len(all_books) == 1
        assert get_id(all_books[0]) == 1
        assert get_titlu(all_books[0]) == "ceva"


def test_delete_book():

        all_books = []
        add_book(all_books,1, "ceva", "altceva", "cineva")
        add_book(all_books, 2, "inca ceva", "inca altceva", "altcinva")

        delete_book(all_books,1)
        assert len(all_books) == 1
        assert get_id(all_books[0]) == 2


def test_book_operations():
    test_add_book()
    test_delete_book()
