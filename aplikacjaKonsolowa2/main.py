class Osoba:

    liczba_instancji = 0

    def __init__(self, id=0, imie=''):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def kopiuj(self, o):
        return Osoba(o.__id, o.__imie)


Ktoś = Osoba()
Coś = Osoba(2,"lawndl")
print(Ktoś.__dict__)
print(Coś.__dict__)
Jakoś = Coś.kopiuj(Coś)
print(Jakoś.__dict__)
print(Osoba.liczba_instancji)