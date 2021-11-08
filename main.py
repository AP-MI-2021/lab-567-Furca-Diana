from Tests.testAll import RunAllTests
from UI.console import runMenu
from UI.command_line_console import runMenu2
from Logic.CRUD import adaugarezervare


def alegmeniu():
    print("1. Alege meniul standard- Interfata 1.")
    print("2. Alege meniul in care poti apela mai multe functii in acelasi timp!- Interfata 2")


def main():
    RunAllTests()
    lista = []
    lista = adaugarezervare("1", "Monica", "economy", 200, "da", lista)
    lista = adaugarezervare("2", "Monica", "economy plus", 390, "da", lista)
    lista = adaugarezervare("3", "Liviu", "economy", 250, "nu", lista)
    lista = adaugarezervare("4", "Denisa", "business", 550, "nu", lista)
    lista = adaugarezervare("5", "Ada", "economy plus", 800, "da", lista)

    while True:
        alegmeniu()
        optiune = input("Alege interfata: ")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runMenu2(lista)
        elif optiune == "h":
            print("Alege un meniu dintre Interfata 1 si Interfata 2:")
        elif optiune == "x":
            break
        else:
            print("Optiune greasita! Reincercati!")


if __name__ == '__main__':
    main()
