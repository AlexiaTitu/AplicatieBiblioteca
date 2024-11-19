from libraryapp.domain.cliententity import create_client, get_id, set_id, get_nume, set_nume, get_cnp, set_cnp


def test_create_client():
    client = create_client(1, "Petre",123)
    assert client == {"id": 1, "nume": "Petre", "cnp": 123}

def test_get_id():
    client = create_client(2, "Mihai", 124)
    assert get_id(client) == 2


def test_set_id():
    client = create_client(3, "Ioana", 125)
    set_id(client, 10)
    assert client["id"] == 10


def test_get_nume():
    client= create_client(4, "Mihaela", 126)
    assert get_nume(client) == ("Mihaela")


def test_set_nume():
    client = create_client(5, "Ioana", 127)
    set_nume(client, "Maria")
    assert client["nume"] == "Maria"


def test_get_cnp():
    client = create_client(6, "Alexia", 128)
    assert get_cnp(client) == 128


def test_set_cnp():
    client = create_client(7, "Eduard", 567)
    set_cnp(client, "123")
    assert client["cnp"] == "123"



def test_cliententity():
    test_create_client()
    test_get_id()
    test_set_id()
    test_get_nume()
    test_set_nume()
    test_get_cnp()
    test_set_cnp()

