
# Aria = pi * r ** 2


## CONVENTIE -> LITERE MARI == CONSTANTA
PI = 3.14
print(PI)


while True:
    raza = input("Introduceti raza cercului \n")
    try:
        raza = float(raza)
        aria = PI * raza ** 2
        print("Aria cercului este:", aria)
    except:
        print("Raza introdusa nu se poate transforma intr-un numar")
