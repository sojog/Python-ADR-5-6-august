# Programare Orientata Obiect


pret = 20

def incrementare(x):
    return x + 2

def calcul_tva(pret):
    return pret + 0.21 * pret


## Clasa este un fel de sablon
class Produs:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

    def incrementeaza_pret(self, procent):
        self.pret = self.pret + procent * self.pret / 100


## Obiectul este o instanta
p1 = Produs("Telefon", 1000)
print(p1, p1.nume, p1.pret)

p1.incrementeaza_pret(20)
print(p1, p1.nume, p1.pret)


p2 = Produs("Agenda", 10)
print(p2,  p2.nume, p2.pret)