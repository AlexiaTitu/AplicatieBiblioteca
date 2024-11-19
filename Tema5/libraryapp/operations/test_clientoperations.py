from Tema5.libraryapp.domain.cliententity import get_id, get_nume
from Tema5.libraryapp.operations.clientoperations import delete_client, add_client

def test_add_client():
        all_clients = []
        add_client(all_clients, 1, "Eduard Antonescu", 123)
        assert len(all_clients) == 1
        assert get_id(all_clients[0]) == 1
        assert get_nume(all_clients[0]) == "Eduard Antonescu"


def test_delete_client():

        all_clients = []
        add_client(all_clients,1,  "Carina", 253)
        add_client(all_clients, 2, "Darius", 456 )

        delete_client(all_clients,1)
        assert len(all_clients) == 1
        assert get_id(all_clients[0]) == 2


def test_client_operations():
    test_add_client()
    test_delete_client()
