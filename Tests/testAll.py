from Tests.testCRUD import testadaugarezervare, teststergerezervare, testmodificarezervarea
from Tests.testDomain import testrezervare
from Tests.testFunctionalitati import testTrecereRezervari

def RunAllTests():
    testrezervare()
    testadaugarezervare()
    teststergerezervare()
    testmodificarezervarea()
    testTrecereRezervari()

