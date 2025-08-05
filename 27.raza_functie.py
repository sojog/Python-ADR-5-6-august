## CONVENTIE -> LITERE MARI == CONSTANTA
PI = 3.14

def calculeaza_aria(raza):
    return PI * raza ** 2


while True:
    raza = input("Introduceti raza cercului \n")
    try:
        raza = float(raza)
        aria = calculeaza_aria(raza)
        print("Aria cercului este:", aria)
    except:
        print("Raza introdusa nu se poate transforma intr-un numar")