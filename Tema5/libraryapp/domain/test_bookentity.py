from libraryapp.domain.bookentity import create_book, get_id, set_id, get_titlu, set_titlu, get_descriere, set_descriere, get_autor, set_autor


def test_create_book():
    book = create_book(1, "ceva", "inca ceva", "cineva")
    assert book == {"id": 1, "titlu": "ceva", "descriere": "inca ceva", "autor": "cineva"}

def test_get_id():
    book = create_book(2, "Alt titlu", "Alta descriere", "Alt autor")
    assert get_id(book) == 2


def test_set_id():
    book = create_book(3, "Titlu", "Descriere", "Autor")
    set_id(book, 10)
    assert book["id"] == 10


def test_get_titlu():
    book = create_book(4, "Titlu test", "Descriere test", "Autor test")
    assert get_titlu(book) == "Titlu test"


def test_set_titlu():
    book = create_book(5, "Titlu vechi", "Descriere", "Autor")
    set_titlu(book, "Titlu nou")
    assert book["titlu"] == "Titlu nou"


def test_get_descriere():
    book = create_book(6, "Titlu", "Descriere test", "Autor")
    assert get_descriere(book) == "Descriere test"


def test_set_descriere():
    book = create_book(7, "Titlu", "Descriere veche", "Autor")
    set_descriere(book, "Descriere noua")
    assert book["descriere"] == "Descriere noua"


def test_get_autor():
    book = create_book(8, "Titlu", "Descriere", "Autor test")
    assert get_autor(book) == "Autor test"


def test_set_autor():
    book = create_book(9, "Titlu", "Descriere", "Autor vechi")
    set_autor(book, "Autor nou")
    assert book["autor"] == "Autor nou"

def test_bookentity():
    test_create_book()
    test_get_id()
    test_set_id()
    test_get_titlu()
    test_set_titlu()
    test_get_descriere()
    test_set_descriere()
    test_get_autor()
    test_set_autor()
