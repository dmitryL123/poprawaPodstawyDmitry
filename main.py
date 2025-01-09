import random

class Kolejka:
    def __init__(self):
        self.queue = []

    def dodajDoKolejki(self, klient):
        self.queue.append(klient)

    def usunZKolejki(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def wyswietl(self):
        return self.queue

class Stos:
    def __init__(self):
        self.stack = []

    def dodajDoStosu(self, klient):
        self.stack.append(klient)

    def usunZeStosu(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def wyswietl(self):
        return self.stack

class Miejsca:
    def __init__(self):
        self.miejsca = [[0 for _ in range(10)] for _ in range(10)]

    def wybierzMiejsce(self):
        miejscaWolne = [(i,j) for i in range(10) for j in range(10) if self.miejsca[i][j] == 0]
        if miejscaWolne:
            miejsce = random.choice(miejscaWolne)
            self.miejsca[miejsce[0]][miejsce[1]] = 1
            return miejsce
        return None

    def pokazMiejsca(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.miejsca])

class Kino:
    def __init__(self):
        self.historia = Stos()
        self.kolejka = Kolejka()
        self.miejsca = Miejsca()

    def dodajKlienta(self, imie, nazwisko):
        klient = {"imie": imie, "nazwisko": nazwisko}
        self.kolejka.dodajDoKolejki(klient)

    def obsluz(self):
        klient = self.kolejka.usunZKolejki()
        if klient:
            miejsce = self.miejsca.wybierzMiejsce()
            if miejsce:
                self.historia.dodajDoStosu({"klient": klient, "miejsce": miejsce})
                return f"Klient: {klient['imie']} {klient['nazwisko']} został obsłuzony. Przydzielono miescje {miejsce}"
            else:
                return "Brak wolnych miejsc"
        return "Brak klientów w kolejce"

    def wyswietlKolejke(self):
        return self.kolejka.wyswietl()

    def wyswietlMiejsca(self):
        return self.miejsca.pokazMiejsca()

    def pokazHistorie(self):
        return self.historia.wyswietl()



def main():
    kino = Kino()
    while True:
        print("\nMenu")
        print("1. Dodaj klienta")
        print("2. Obsłuż klienta")
        print("3. Sprawdź stan kolejki")
        print("4. Pokaż historie obsłuzonych klientów")
        print("5. Pokaż miejsca na sali")
        print("6. Zakończ program")

        wybor = input("Wybierz opcje: ")

        if wybor == "1":
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            kino.dodajKlienta(imie, nazwisko)
        elif wybor == "2":
            print(kino.obsluz())
        elif wybor == "3":
            print(kino.wyswietlKolejke())
        elif wybor == "4":
            print(kino.pokazHistorie())
        elif wybor == "5":
            print(kino.wyswietlMiejsca())
        elif wybor == "6":
            print("Zakończenie programu")
            break
if __name__ == '__main__':
    main()