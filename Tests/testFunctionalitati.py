from Domain.companie_aeriana import getclasa, getid, getpret
from Logic.CRUD import adaugarezervare, getById
from Logic.diverseFunctionalitati import TrecereRezervari, ieftinirePret


def testTrecereRezervari():
    lista = []
    lista = adaugarezervare("1", "Liviu", "economy", 500, "da", lista)
    lista = adaugarezervare("2", "Liviu", "economy plus", 700, "da", lista)
    lista = adaugarezervare("3", "Anca", "business", 300, "nu", lista)

    lista = TrecereRezervari("Liviu", lista)

    assert getclasa(getById("1", lista)) == "economy plus"
    assert getclasa(getById("2", lista)) == "business"


def testieftinirePret():

    lista = []
    lista = adaugarezervare("1", "Diana", "economy", 120, "da", lista)
    lista = adaugarezervare("2", "Oana", "economy plus", 230, "da", lista)
    lista = adaugarezervare("3", "Cami", "business", 340, "da", lista)

    lista = ieftinirePret(10, lista)

    assert getpret(getById("1", lista)) == 108
    assert getpret(getById("2", lista)) == 207
    assert getpret(getById("3", lista)) == 306