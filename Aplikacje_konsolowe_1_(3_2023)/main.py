class Film:
    def __init__(self):
        self._tytul = ""  # Pole na tytuł filmu, początkowo pusty
        self._liczba_wypozyczen = 0  # Pole na liczbę wypożyczeń, początkowo 0

    # Setter - ustawianie tytułu filmu
    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł jest za długi, maksymalnie 20 znaków.")

    # Getter - pobieranie tytułu filmu
    def get_tytul(self):
        return self._tytul

    # Getter - pobieranie liczby wypożyczeń
    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    # Inkrementacja liczby wypożyczeń
    def inkrementuj_wypozyczenia(self):
        self._liczba_wypozyczen += 1


# Test aplikacji
if __name__ == "__main__":
    # Inicjalizacja obiektu
    film = Film()

    # Wyświetlenie początkowych wartości pól
    print("Początkowy tytuł filmu:", film.get_tytul())
    print("Początkowa liczba wypożyczeń:", film.get_liczba_wypozyczen())

    # Test metody set - ustawienie tytułu
    film.set_tytul("Incepcja")
    print("Tytuł po ustawieniu:", film.get_tytul())

    # Test metody get - pobranie tytułu
    aktualny_tytul = film.get_tytul()
    print("Pobrany tytuł filmu:", aktualny_tytul)

    # Test metody inkrementacji
    print("Liczba wypożyczeń przed inkrementacją:", film.get_liczba_wypozyczen())
    film.inkrementuj_wypozyczenia()
    print("Liczba wypożyczeń po inkrementacji:", film.get_liczba_wypozyczen())
