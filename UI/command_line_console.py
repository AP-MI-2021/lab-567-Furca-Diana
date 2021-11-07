from Logic.CRUD import adaugarezervare, stergerezervare
from UI.console import showAll


def oneLineAddShowallDelete(elem, lista):
    elem = elem.split(";")
    i = 0
    while i < len(elem):
        if elem[i] == "Adauga":
            lista = adaugarezervare(elem[i+1], elem[i+2], elem[i+3], elem[i+4], elem[i+5], lista)
            i = i + 5
        elif elem[i] == "Afiseaza toate rezervarile":
            showAll(lista)
        elif elem[i] == "Sterge":
            lista = stergerezervare(elem[i+1], lista)
        i = i + 1
    return lista


def uiOneLine(lista):
    elem = input("Dati comanda cu parametrii corespunzatori: la afisare trebuie id, nume, clasa, pret, checkin/"
                 "la stergere trebuie id: ")
    return oneLineAddShowallDelete(elem, lista)


def printMeniu():
    print("1. Adauga/ Sterge/ Afiseaza toate rezervarile")
    print("x. Iesire")
    print("help. Printare meniu")


def runMenu2(lista):
    while True:
        printMeniu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "help":
            printMeniu()
        elif optiune == "1":
            lista = uiOneLine(lista)
        elif optiune == "x":
            print("Programul a fost incheiat")
            break
        else:
            print("Optiune gresita. Reincercati")
