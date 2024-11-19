def create_client(id, nume, cnp):
    return {"id":id, "nume":nume, "cnp":cnp}

def get_id(client):
    """
    Functie care obtine id-ul unui anumit client din lista
    """
    return client["id"]

def set_id(client, id):
    """
    Functie care seteaza un alt id pentru un anumit client din lista
    """
    client["id"] = id

def get_nume(client):
    return client["nume"]

def set_nume(client, nume):
    client["nume"] = nume

def get_cnp(client):
    return client["cnp"]

def set_cnp(client, cnp):
    client["cnp"] = cnp

