from Domain.companie_aeriana import getnume, getid, getclasa, getpret, getcheckin
from Logic.CRUD import adaugarezervare, getById, stergerezervare


def testadaugarezervare():
    lista = []
    lista = adaugarezervare("1", "Monica","business", 500, "da", lista)

    assert len(lista) == 1
    assert getid(getById("1", lista)) == "1"
    assert getnume(getById("1", lista)) == "Monica"
    assert getclasa(getById("1",lista)) == "business"
    assert getpret(getById("1",lista)) == 500
    assert getcheckin(getById("1",lista)) == "da"

def teststergerezervare():
    lista = []
    lista = adaugarezervare("1", "Monica", "business", 500, "da", lista)
    lista = adaugarezervare("2", "Livia", "economy", 400, "da", lista)

    lista = stergerezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergerezervare("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None
