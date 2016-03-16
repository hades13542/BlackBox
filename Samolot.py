import random
import threading
from Error import Error
import sys


class Samolot:
    def __init__(self, nazwa, odleglosc, paliwo, predkosc):
        self.nazwa = nazwa
        self.odleglosc = odleglosc
        self.paliwo = paliwo
        self.predkosc = predkosc
        self.czas = (self.odleglosc / self.predkosc) * 60  # czas w min
        self.stop = None

    def zaburzenia(self):
        spalanie = random.randint(1, 10)
        wachaniePredkosci = random.randint(-5, 5)
        self.paliwo -= spalanie
        self.predkosc += wachaniePredkosci
        self.odleglosc -= self.predkosc / 60
        print("Obecnu stan paliwa {} [l]".format(self.paliwo))
        print("Obecna predkosc {} [km/h]".format(self.predkosc))

    def print(self):
        print("Odleglosc: {} [km]".format(self.odleglosc))
        print("Paliwo: {} [l]".format(self.paliwo))
        print("Prędkość {} [km/h]".format(self.predkosc))
        print("Czas {} [min]".format(self.czas))
        print("W 1 min przelecisz {0} [km]".format(self.predkosc / 60))
        print("---------------------------------")

    def poprawnosc(self):
        # TODO:SPRAWDZENIE POPRAWNOSCI DANYCH NA WEJSCIU
        return 0

    def sprawdzanie(self):
        try:
            if self.paliwo < 30:
                print("Ostrzezenie paliwo się kończy!")
            if self.paliwo <= 0:
                raise Error("BRAK PALIWA!")
            if self.odleglosc < 0:
                print("Dotarłeś do celu")
            if self.predkosc <= 0:
                self.predkosc = 1
            if self.czas < 0 and self.odleglosc > 0:
                raise Error("cos tu ewidentnie nie dziala!")
        except Error as e:
            print(e)
            self.stop = True
            sys.exit()

    def run(self):
        self.symulacja()

    def symulacja(self):
        global timer
        self.zaburzenia()
        self.sprawdzanie()
        timer = threading.Timer(5, self.symulacja).start()
        if self.stop == True:
            timer.cancel()
