from Tema5.libraryapp.domain.bookentity import get_id
from Tema5.libraryapp.domain.bookentity import create_book

def add_book(all_books, id, titlu, descriere, autor):
    """
    Functie care primeste ca parametri o lista all_books, un id, un titlu, o descriere si un autor
    Aceasta creeaza o noua carte, cu id, titlu, descriere si autor si o adauga listei all_books

    """
    book = create_book(id, titlu, descriere, autor)
    all_books.append(book)

def delete_book(all_books,idbook):
    """
    Functie care primeste doi parametri: lista all_books si un parametru idbook
    Functia parcurge lista all_books si cu ajutorul functiei get_id(book), care gaseste id-ul cartii
    compara, id-ul acesteia cu cel instrodus de la tastatura. Odata ce ascestea coincid,
    functia sterge cartea cu toate datele acesteia din lista all_books

    """
    for book in all_books:
        if get_id(book) == idbook:
            all_books.remove(book)
    return None