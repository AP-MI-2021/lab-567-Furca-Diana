from Domain.companie_aeriana import creeaza_rezervare, getnume, getid, getclasa, getpret, getcheckin


def TrecereRezervari(numetrecere, lista):
    """
    Trecerea tuturor rezervarilor facute pe un nume citit, la o clasa superioara
    :param numetrecere: string, numele persoanei pe al carei nume s-a facut rezervarea
    :param lista: lista de rezervari
    :return: lista cu rezervari, dupa ce s-a realizat modificarea claselor
    """
    listaNoua = []

    for rezervare in lista:

        if getnume(rezervare) == numetrecere and getclasa(rezervare) == "economy":
            rezervareNoua = creeaza_rezervare(
                getid(rezervare),
                getnume(rezervare),
                "economy plus",
                getpret(rezervare),
                getcheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)

        elif getnume(rezervare) == numetrecere and getclasa(rezervare) == "economy plus":
            rezervareNoua = creeaza_rezervare(
                getid(rezervare),
                getnume(rezervare),
                "business",
                getpret(rezervare),
                getcheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)

        elif getnume(rezervare) == numetrecere and getclasa(rezervare) == "business":
            listaNoua.append(rezervare)
    return listaNoua

def ieftinirePret(procentaj, lista):
    '''
    Determina ieftinirea tuturor rezervarilor cu checkin facut, cu un procentaj citit de la tastatura, si o aplica preturilor
    :param procentaj: procentul cu care se ieftineste rezervarea
    :param lista:lista de rezervari
    :return: lista cu preturile ieftinite
    '''
    if procentaj < 0:
        raise ValueError("Ati adaugat un numar negativ.Procentajul trebuie sa fie un numar pozitiv.")

    listaNoua = []

    for rezervare in lista:
        if getcheckin(rezervare) == "da":
            reducere = (procentaj//100) * getpret(rezervare)
            rezervareNoua = creeaza_rezervare(
                getid(rezervare),
                getnume(rezervare),
                getclasa(rezervare),
                getpret(rezervare)-reducere,
                getcheckin(rezervare)
            )

            listaNoua.append(rezervareNoua)

        else:
            listaNoua.append(rezervare)
    return listaNoua