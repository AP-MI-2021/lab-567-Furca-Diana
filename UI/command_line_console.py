from Logic.CRUD import adaugarezervare, stergerezervare
from UI.console import showAll


def oneLine(lista):
    while True:
        lineCom = input('Dati comanda(comenzile separate prin ";" , elementele prin ",": )')
        lineCom = lineCom.split(';')
        for l in lineCom:
            l = l.split(',')
            if l[0] == 'add':
                if len(l) == 6:
                    try:
                        id = l[1]
                        nume = l[2]
                        clasa = l[3]
                        pret = float(l[4])
                        checkin = l[5]
                        lista = adaugarezervare(id, nume, clasa, pret, checkin, lista)
                    except ValueError as ve:
                        print(f'Eroare:{ve}')
                else:
                    print('Eroare, numar invalid de parametrii')
            elif l[0] == "showall":
                showAll(lista)
            elif l[0] == "delete":
                if len(l) == 2:
                    try:
                        id = l[1]
                        lista = stergerezervare(id, lista)
                    except ValueError as ve:
                        print(f'Eroare:{ve}')
                else:
                    print('Eroare, numar invalid de parametrii')
            else:
                print('Comanda gresita, reincercati')


def printMeniu2():
    print("1. Adauga o rezervare/ Sterge o rezervare/ Afiseaza toate rezervarile")
    print("x. Iesire")
    print("h. Help.")


def runMenu2(lista):
    while True:
        printMeniu2()
        optiune = input("Alegeti optiunea: ")
        if optiune == "help":
            print("Daca vreti sa adaugati o rezervare, scrieti comanda add, urmata de id, nume, clasa, pret, checkin")
            print("Daca vreti sa stergeti o rezervare, scrieti comanda delete, urmata de id")
            print("Daca vreti sa afisati toata lista, scrieti showall")

        elif optiune == "1":
            lista = oneLine(lista)
        elif optiune == "x":
            print("Programul a fost incheiat")
            break
        else:
            print("Optiune gresita. Reincercati")
