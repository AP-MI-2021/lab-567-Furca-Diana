from Tests.testAll import RunAllTests
from UI.console import runMenu
from UI.command_line_console import runMenu2
from Logic.CRUD import adaugarezervare


def optiuni():
    print("1. Alege meniul standard.")
    print("2. Alege meniul in care poti apela mai multe functii in acelasi timp!")


def main():
    RunAllTests()
    lista = []
    lista = adaugarezervare("1", "Monica", "economy", 200, "da", lista)
    lista = adaugarezervare("2", "Monica", "economy plus", 390, "da", lista)
    lista = adaugarezervare("3", "Liviu", "economy", 250, "nu", lista)
    lista = adaugarezervare("4", "Denisa", "business", 550, "nu", lista)
    lista = adaugarezervare("5", "Ada", "economy plus", 800, "da", lista)
    optiuni()
    optiune = input("Alege main-ul pe care vrei sa il rulezi: ")

    while True:
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runMenu2(lista)
        else:
            print("Meniul selectat nu exista! Reincercati.")
        meniuNou = input("Vreti sa schimbati meniul? da/nu:")
        if meniuNou.lower() == "da":
            optiuni()
            optiune = input("Alege main-ul pe care vrei sa il rulezi")
        elif meniuNou.lower() == "nu":
            break
        else:
            print("Meniul selectat nu exista! Reincercati.")

main()
