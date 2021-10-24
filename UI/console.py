from Domain.companie_aeriana import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare


def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("a.Afisarea rezervarilor")
    print("x.Iesire")


def uiAdaugaRezervare(lista):
        id = input("Dati id-ul:")
        nume = input("Dati nume:")
        clasa = input("Dati clasa:")
        pret = int(input("Dati pretul:"))
        checkin = input("Dati checkin:")
        return adaugarezervare(id, nume, clasa, pret, checkin, lista)


def uiStergeRezervare(lista):
        id = input("Dati id-ul rezervarii pe care vreti sa o stergeti:")
        return stergerezervare(id, lista)


def uiModificaRezervare(lista):
        id = input("Dati id-ul rezervarii de modificat:")
        nume = input("Dati numele rezervarii de modificat:")
        clasa = input("Dati clasa rezervarii de modificat:")
        pret = int(input("Dati pretul rezervarii de modificat:"))
        checkin = input("Dati checkin-ul rezervarii ce trebuie modificata:")
        return modificarezervare(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
        for rezervare in lista:
            print(toString(rezervare))


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
            elif optiune == "a":
                showAll(lista)
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")