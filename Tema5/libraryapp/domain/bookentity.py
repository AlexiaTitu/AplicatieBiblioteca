
def create_book(id, titlu, descriere, autor):
    return {"id":id, "titlu":titlu, "descriere":descriere, "autor":autor}

def get_id(book):
    """
    Functie care obtine id-ul unei anumite carti din lista
    """
    return book["id"]

def set_id(book, id):
    """
    Functie care seteaza un alt id pentru o anumita carte din lista
    """
    book["id"] = id

def get_titlu(book):
    return book["titlu"]

def set_titlu(book, titlu):
    book["titlu"] = titlu

def get_descriere(book):
    return book["descriere"]

def set_descriere(book, descriere):
    book["descriere"] = descriere

def get_autor(book):
    return book["autor"]

def set_autor(book, autor):
    book["autor"] = autor