from Tests.testCRUD import testadaugarezervare, teststergerezervare, testmodificarezervarea
from Tests.testDomain import testrezervare
from Tests.testFunctionalitati import testTrecereRezervari, testMaxPretPerClasa, testOrdonareDescrescatorDupaPret


def RunAllTests():
    testrezervare()
    testadaugarezervare()
    teststergerezervare()
    testmodificarezervarea()
    testTrecereRezervari()
    testMaxPretPerClasa()
    testOrdonareDescrescatorDupaPret()

