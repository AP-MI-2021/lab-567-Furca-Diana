from Domain.companie_aeriana import *


def adaugarezervare(id, nume, clasa, pret, checkin, lista):
    """
    Adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: lista ce contine elementele vechi si noua rezervare
    """
    if getById(id, lista) is not None:
        raise ValueError("Acest id deja exista.")
    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def getById(id, lista):
        """
        Furnizeaza rezervarea cu id-ul dat dintr-o lista
        :param id: string
        :param lista: lista cu rezervari
        :return: rezervarea data cu id-ul dintr-o lista, in caz contrar None
        """
        for rezervare in lista:
            if getid(rezervare) == id:
                return rezervare
        return None


def stergerezervare(id, lista):
        """
        Sterge rezervarea cu id-ul corespunzator celui dat
        :param id: id-ul rezervarii care se va sterge
        :param lista: lista cu rezervari
        :return: lista obtinuta dupa stergerea unei rezervari
        """
        if getById(id, lista) is None:
            raise ValueError("Acst id nu exista")
        return [rezervare for rezervare in lista if getid(rezervare) != id]
    # parcurg lista, daca rezervarea curenta nu trebuie stearsa, o punem in noua lista


def modificarezervare(id, nume, clasa, pret, checkin, lista):
        '''
        Modifica o rezervare dupa un id
        :param id: id-ul rezervarii
        :param nume:numele rezervarii
        :param clasa:clasa rezervarii
        :param pret:pretul rezervarii
        :param checkin:checkin ul rezervarii
        :param lista:lista de rezervari
        :return:lista modificata
        '''
        if getById(id, lista) is None:
            raise ValueError("Acest id nu exista")
        listaNoua = []
        for rezervare in lista:
            if getid(rezervare) == id:
                rezervareNoua = creeaza_rezervare(id, nume, clasa, pret, checkin)
                listaNoua.append(rezervareNoua)
            else:
                listaNoua.append(rezervare)
        return listaNoua
