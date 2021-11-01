from Tests.testAll import RunAllTests
from UI.console import runMenu
from Logic.CRUD import adaugarezervare

def main():
    RunAllTests()
    lista = []
    lista = adaugarezervare("1", "Monica", "economy", 200, "da", lista)
    lista = adaugarezervare("2", "Monica", "economy plus", 390, "da", lista)
    lista = adaugarezervare("3", "Liviu", "economy", 250, "nu", lista)
    lista = adaugarezervare("4", "Denisa", "business", 550, "nu", lista)
    lista = adaugarezervare("5", "Ada", "economy plus", 800, "da", lista)
    runMenu(lista)

main()
