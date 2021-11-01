from Domain.companie_aeriana import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare
from Logic.diverseFunctionalitati import TrecereRezervari, ieftinirePret


def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervarilor facute pe un nume citit, la o clasa superioara")
    print("5.Ieftinirea tuturor rezervarilor la care s-a facut checkin, cu un procentaj citit")
    print("a.Afisarea rezervarilor")
    print("x.Iesire")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul:")
        nume = input("Dati nume:")
        clasa = input("Dati clasa:")
        pret = float(input("Dati pretul:"))
        checkin = input("Dati checkin:")
        return adaugarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii pe care vreti sa o stergeti:")
        return stergerezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat:")
        nume = input("Dati numele rezervarii de modificat:")
        clasa = input("Dati clasa rezervarii de modificat:")
        pret = float(input("Dati pretul rezervarii de modificat:"))
        checkin = input("Dati checkin-ul rezervarii ce trebuie modificata:")
        return modificarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiTrecereRezervari(lista):
    try:
        numetrecere = input("Dati numele persoanei ale carei rezervari sa fie trecute la o clasa superioara:")
        modificare = TrecereRezervari(numetrecere, lista)
        showAll(modificare)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiIeftinirePret(lista):
    procentaj = int(input("Dati procentul cu care o sa se ieftineasca pretul rezervarilor cu checkin facut :"))
    rezultat = ieftinirePret(procentaj, lista)
    showAll(rezultat)

    #showAll(rezultat)
    #return lista


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiTrecereRezervari(lista)
        elif optiune == "5":
            lista = uiIeftinirePret(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")