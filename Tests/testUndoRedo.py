from Domain.companie_aeriana import getid
from Logic.CRUD import adaugarezervare, stergerezervare


def testUndoRedo():

    lista = []
    undoList = []
    redoList = []

    # 1 adauga o rezervare

    rezultat = adaugarezervare("1", "Diana", "business", 550, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 2 adauga o rezervare

    rezultat = adaugarezervare("2", "Anca", "economy", 390, "da", lista)
    undoList.append(lista)
    lista = rezultat

    # 3 adauga o rezervare

    rezultat = adaugarezervare("3", "Teodora", "economy plus", 320, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    # 4 undo scoate ultima rezervare

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    #print(getid(lista[1]))
    assert getid(lista[1]) == "2"
    assert getid(lista[0]) == "1"

    # 5 undo scoate penultima rezervare

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getid(lista[0]) == "1"
    assert undoList == [[]]

    # 6 undo scoate prima rezervare

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []

    # 7 undo care nu face nimic

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []

    # 8 adaugam 3 rezervari

    rezultat = adaugarezervare("1", "Bogdan", "business", 690, "nu", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = adaugarezervare("2", "Horea", "economy plus", 500.0, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugarezervare("3", "Victor", "economy", 350, "da", lista)
    undoList.append(lista)
    lista = rezultat
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 9 facem redo, care practic nu se poate face, lista de redo e goala

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 10 2 undo, care scot ultimele 2 rezervari

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert getid(lista[1]) == "2"
    assert getid(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 1
    assert getid(lista[0]) == "1"
    assert undoList == [[]]

    # 11 redo, care aduce inapoi penultima rezervare

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) ==1
    assert len(undoList) == 2
    assert len(lista) == 2

    # 12 redo, redo, care aduce inapoi si ultima rezervare

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # 13 se fac 2 undo, ca sa dispara ultimele 2 rezervari

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getid(lista[1]) == "2"
    assert getid(lista[0]) == "1"


    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getid(lista[0]) == "1"
    assert undoList == [[]]

    # 14 adaugam a 4 a rezervare

    rezultat = adaugarezervare("4", "Cristian", "business", 1000.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    # 15 redo, care nu face nimic

    if len(redoList) > 0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2

    # 16 se face undo, dispare ultima rezervare

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(redoList) == 1
    assert len(undoList) == 1

    # 17 undo, dispare si penultima

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(redoList) == 2
    assert len(undoList) == 0

    # 18 2 redo, cele doua rezervari revin in lista

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    # 19 ultimul redo care nu face nimic

    if len(redoList) >0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2