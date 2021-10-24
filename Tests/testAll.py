from Tests.testCRUD import testadaugarezervare, teststergerezervare
from Tests.testDomain import testrezervare


def RunAllTests():
    testrezervare()
    testadaugarezervare()
    teststergerezervare()