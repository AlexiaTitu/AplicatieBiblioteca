from libraryapp.domain.cliententity import get_id
from libraryapp.domain.cliententity import create_client

def add_client(all_clients, id, nume, cnp):
    """
    Functie care primeste ca parametri o lista all_books, un id, un titlu, o descriere si un autor
    Aceasta creeaza o noua carte, cu id, titlu, descriere si autor si o adauga listei all_books

    """
    client = create_client(id, nume, cnp)
    all_clients.append(client)

def delete_client(all_clients,idclient):
    """
    Functie care primeste doi parametri: lista all_books si un parametru idbook
    Functia parcurge lista all_books si cu ajutorul functiei get_id(book), care gaseste id-ul cartii
    compara, id-ul acesteia cu cel instrodus de la tastatura. Odata ce ascestea coincid,
    functia sterge cartea cu toate datele acesteia din lista all_books

    """
    for client in all_clients:
        if get_id(client) == idclient:
            all_clients.remove(client)
    return None