class Notatka:
    __licznik = 0
    def __init__(self, tytul="", tresc=""):
        Notatka.__licznik += 1
        self.__id = Notatka.__licznik
        self._tytul = tytul
        self._tresc = tresc

    def pokaz(self):
        return self._tytul, self._tresc

    def diagnoza(self):
        return str(self.__id) + "; " + self._tytul + "; " + self._tresc

if __name__ == "__main__":
    # Tworzenie dwóch notatek
    notatka1 = Notatka("Zakupy", "Kupić chleb, mleko i jajka.")
    notatka2 = Notatka("Spotkanie", "Spotkanie z klientem w poniedziałek o 10:00.")

    # Wyświetlenie notatek
    print("Notatka 1:")
    print(notatka1.pokaz())
    print("\nDiagnostyka notatki 1:")
    print(notatka1.diagnoza())

    print("\nNotatka 2:")
    print(notatka2.pokaz())
    print("\nDiagnostyka notatki 2:")
    print(notatka2.diagnoza())