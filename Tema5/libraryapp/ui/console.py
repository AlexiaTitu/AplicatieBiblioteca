from libraryapp.operations.bookoperations import add_book
from libraryapp.operations.bookoperations import delete_book
from libraryapp.operations.clientoperations import delete_client, add_client

def ui_add_book(all_books):
    """
    Functia afiseaza pe ecran parametrii care utilizator trebuie sa-i indroduca si primeste
    un id, un titlu, o descriere si un autor. Cu acesti parametri se apeleaza functia add_book
    care adauga onoua carte la lista
    """
    id=int(input("Enter a book id: "))
    titlu=input("Enter titlu: ")
    descriere=input("Enter descriere: ")
    autor=input("Enter autor: ")
    add_book(all_books, id, titlu, descriere, autor)

def ui_add_client(all_clients):
    """
    Functia afiseaza pe ecran parametrii care utilizator trebuie sa-i indroduca si primeste
    un id, un titlu, o descriere si un autor. Cu acesti parametri se apeleaza functia add_book
    care adauga onoua carte la lista
    """
    id=int(input("Enter a client id: "))
    nume=input("Enter nume: ")
    cnp=int(input("Enter cnp: "))
    add_client(all_clients, id, nume, cnp)

def run_console():
    """
    Functie care afiseaza pe ecran meniul cu optiunile sale. Aceasta primeste de la tastatura
    optiunea pe care utilizatorul doreste s-o apeleze, si apeleaza functia corespunzatoare
    acelei optiuni
    """
    all_books = []
    all_clients = []
    while True:
        print("1-Afisare carti \n 2-Adaugare carti \n 3-Stergere carti \n 4-Modificare carte \n 5-Afisare clienti \n 6-Adaugare client \n 7-Stergere client \n 8-Modificare client \n x-Exit")
        optiune = input("Enter your option: ")
        try:
            if optiune == "1":
              print(all_books)
            elif optiune == "2":
                ui_add_book(all_books)
            elif optiune == "3":
                idbook = int(input("Enter your book id: "))
                delete_book(all_books,idbook)
            elif optiune == "5":
                print(all_clients)
            elif optiune == "6":
                ui_add_client(all_clients)
            elif optiune == "7":
                idclient = int(input("Enter your client id: "))
                delete_client(all_clients,idclient)
            elif optiune == "x":
                print("Bye")
                break
            else:
                raise ValueError
        except ValueError:
            print("Optiune invalida. Te rog sa alegi 1, 2, 3, 4, 5, 6, 7, 8 sau x.")