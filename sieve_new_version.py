class Sito:
    def __init__(self, granica, liczba, p=False):
        self.granica = granica
        self.liczba = liczba
        self.lista =[]
        self.p = p

    def odsiej(self):
        self.p = True
        #tworzenie listy na podstawie granicy
        for i in range(2, self.granica + 1):
            self.lista.append(i)
        #odsiewanie
        for k in range(2, self.granica+1):
            for j in self.lista:
                if j % k == 0:
                    if j != k:
                        self.lista.remove(j)

        return self.lista

    def wyswietl(self):
        if self.lista:
            print(self.lista)

    def sprawdz(self):
            if self.liczba in range(2, self.granica+1):
                if self.liczba in self.lista:
                    print("Liczba jest liczbą pierwszą.")
                else:
                    if self.lista:
                        print("Liczba nie jest liczbą pierwszą.")
                    else:
                        print("Sprawdzanie wykonano przed odsianiem.")
            else:
                if self.p == True:
                    print("Liczby nie ma w podanym zakresie.")
                elif self.p == False:
                    print("Sprawdzenie wykonano przed odsianiem.")


n = int(input("Podaj granicę:\n"))
l = int(input("Podaj liczbę:\n"))
sito1 = Sito(granica=n, liczba=l)

sito1.odsiej()
sito1.sprawdz()
sito1.wyswietl()
