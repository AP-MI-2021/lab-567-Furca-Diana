def creeaza_rezervare(id, nume, clasa, pret, checkin):
    """
    Creeaza un dictionar care contine datele despre o rezervare a unui zbor
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce contine o rezervare
    """
#    return {
#        "id": id,
#        "nume":  nume,
#        "clasa": clasa,
#        "pret": pret,
#        "checkin": checkin
#    }
    return [id, nume, clasa, pret, checkin]
    """lst = []
    lst.append(("id: ", id))
    lst.append(("nume: ", nume))
    lst.append(("clasa: ", clasa))
    lst.append(("pret: ", pret))
    lst.append(("checkin: ", checkin))
    return lst"""

def getid(rezervare):
    """
    Furnizeaza id-ul unei rezervari
    :param rezervare: dictionar care contine o rezervare
    :return: id-ul rezervarii
    """
    #return rezervare["id"]
    #return rezervare[0][1]
    return rezervare[0]


def getnume(rezervare):
    """
    Furnizeaza numele unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: numele rezervarii
    """
    #return rezervare["nume"]
    #return rezervare[1][1]
    return rezervare[1]

def getclasa(rezervare):
    """
    Furnizeaza clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa unei rezervari, aceasta putand fi: economy, economy plus, business
    """
    #return rezervare["clasa"]
    #return rezervare[2][1]
    return rezervare[2]

def getpret(rezervare):
    """
    Furnizeaza pretul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul unei rezervari
    """
    #return rezervare["pret"]
    #return rezervare[3][1]
    return rezervare[3]

def getcheckin(rezervare):
    """
    Furnizeaza checkin-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin-ul unei rezervari, acesta putand fi "da" daca s-a facut sau nu in caz contrar
    """
    #return rezervare["checkin"]
    #return rezervare[4][1]
    return rezervare[4]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {} ".format(
        getid(rezervare),
        getnume(rezervare),
        getclasa(rezervare),
        getpret(rezervare),
        getcheckin(rezervare)
    )