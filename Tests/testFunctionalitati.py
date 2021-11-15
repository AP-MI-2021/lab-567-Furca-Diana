from Domain.companie_aeriana import getclasa, getid, getpret
from Logic.CRUD import adaugarezervare, getById
from Logic.diverseFunctionalitati import TrecereRezervari, ieftinirePret, maxPretPerClasa, ordonareDescrescatorDupaPret, \
    afisareSumaPretPentruFiecareNume


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


def testMaxPretPerClasa():
    lista = []
    lista = adaugarezervare("1", "Feli", "economy", 150, "da", lista)
    lista = adaugarezervare("2", "Daniela", "economy plus", 270, "da", lista)
    lista = adaugarezervare("3", "Horea", "economy", 180, "nu", lista)
    lista = adaugarezervare("4", "Monica", "business", 400, "nu", lista)

    rezultat = maxPretPerClasa(lista)

    assert len(rezultat) == 3   #verific ca dictionarul are 3 chei

    assert rezultat["economy"] == 180
    assert rezultat["economy plus"] == 270
    assert rezultat["business"] == 400


def testOrdonareDescrescatorDupaPret():
    lista = []
    lista = adaugarezervare("1", "Diana", "economy", 150, "da", lista)
    lista = adaugarezervare("2", "Oana", "economy plus", 260, "da", lista)
    lista = adaugarezervare("3", "Claudia", "business", 359, "nu", lista)

    rezultat = ordonareDescrescatorDupaPret(lista)

    assert getid(rezultat[0]) == "3"  # ne intereseaza pozitia
    assert getid(rezultat[1]) == "2"
    assert getid(rezultat[2]) == "1"


def testAfisareSumaPretPentruFiecareNume():
    lista = []
    lista = adaugarezervare("1", "Oana", "economy", 200.00, "da", lista)
    lista = adaugarezervare("2", "Oana", "economy plus", 400, "da", lista)
    lista = adaugarezervare("3", "Aura", "business", 600.00, "nu", lista)
    lista = adaugarezervare("4", "Aura", "economy", 200.00, "nu", lista)

    rezultat = afisareSumaPretPentruFiecareNume(lista)

    assert rezultat["Oana"] == 600.00
    assert rezultat["Aura"] == 800.00