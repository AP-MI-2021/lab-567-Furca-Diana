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
        else:
            listaNoua.append(rezervare)
    return listaNoua


def ieftinirePret(procentaj, lista):
    '''
    Determina ieftinirea tuturor rezervarilor cu checkin facut, cu un procentaj citit de la tastatura,/
     si o aplica preturilor
    :param procentaj: procentul cu care se ieftineste rezervarea
    :param lista:lista de rezervari
    :return: lista cu preturile ieftinite
    '''
    if int(procentaj) < 0 or int(procentaj) > 100:
        raise ValueError("Procentajul trebuie sa fie un numar intre 0 si 100")

    listaNoua = []

    for rezervare in lista:
        if getcheckin(rezervare) == "da":
            reducere = (procentaj/100) * getpret(rezervare)
            rezervareNoua = creeaza_rezervare(        #modificam rezervarea, cream o noua rezervare
                getid(rezervare),                     #preluam id-ul de la rezervarea veche, numele la fel...
                getnume(rezervare),
                getclasa(rezervare),
                getpret(rezervare)-reducere,
                getcheckin(rezervare)
            )

            listaNoua.append(rezervareNoua)    #adaugam in lista noua

        elif getcheckin(rezervare) == "nu":
            listaNoua.append(rezervare)
    return listaNoua


def maxPretPerClasa(lista):
    '''
    Determina, pentru fiecare clasa, pretul maxim
    :param lista: lista de rezervari
    :return: pretul maxim pentru fiecare clasa
    '''

    rezultat = {}              #dictionar gol
    for rezervare in lista:    #mergem prin rezervare, luam pretul si clasa; in dictionar retinem pt fiecare
                               #clasa retinem pretul maxim de la clasa respectiva
                               # daca acel pret e mai mare decat maximul, se inlocuieste maximul cu pretul curent
        pret = getpret(rezervare)
        clasa = getclasa(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat


def ordonareDescrescatorDupaPret(lista):
    '''
    Ordoneaza rezervarile descrescator, in functie de pret
    :param lista: lista de rezervari
    :return: rezervarile in ordine descrescatoare, ordonate in functie de pret
    '''

    return sorted(lista, key=lambda rezervare: getpret(rezervare), reverse=True)

#lista curenta nu se modifica
# sorted are 3 argumente: lista, cheia si reversul
# cheia ne spune dupa ce criteriu sa ordonam
#dandui-se aceasta cheie, pt fiecare elem din lista, sorted va luat in considerare rezultatul calculului de pret, ca sa
#poata face ordonarea
#reverse ne spune daca e crescator sau descrescator