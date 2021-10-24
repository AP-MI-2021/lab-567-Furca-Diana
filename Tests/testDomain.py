

from Domain.companie_aeriana import getid, getnume, creeaza_rezervare, getclasa, getcheckin, getpret

def testrezervare():
    rezervare = creeaza_rezervare("1", "Monica","business", 500, "da")

    assert getid(rezervare) == "1"
    assert getnume(rezervare) == "Monica"
    assert getclasa(rezervare) == "business"
    assert getpret(rezervare) == 500
    assert getcheckin(rezervare) == "da"