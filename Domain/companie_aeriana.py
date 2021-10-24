def creeaza_rezervare(id, nume, clasa, pret, checkin):
    """
    Creeaza un dictionar care contine datele despre o rezervare a unui zbor
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: int
    :param checkin: string
    :return: un dictionar ce contine o rezervare
    """
    return {
        "id": id,
        "nume":  nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getid(rezervare):
    """
    Furnizeaza id-ul unei rezervari
    :param rezervare: dictionar care contine o rezervare
    :return: id-ul rezervarii
    """
    return rezervare["id"]


def getnume(rezervare):
    """
    Furnizeaza numele unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: numele rezervarii
    """
    return rezervare["nume"]


def getclasa(rezervare):
    """
    Furnizeaza clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa unei rezervari, aceasta putand fi: economy, economy plus, business
    """
    return rezervare["clasa"]


def getpret(rezervare):
    """
    Furnizeaza pretul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul unei rezervari
    """
    return rezervare["pret"]


def getcheckin(rezervare):
    """
    Furnizeaza checkin-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin-ul unei rezervari, acesta putand fi "da" daca s-a facut sau nu in caz contrar
    """
    return rezervare["checkin"]


def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {} ".format(
        getid(rezervare),
        getnume(rezervare),
        getclasa(rezervare),
        getpret(rezervare),
        getcheckin(rezervare)
    )