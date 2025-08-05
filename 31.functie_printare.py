# @@@@@@@@@@
# @        @
# @        @
# @@@@@@@@@@


def printeaza_dreptunghi(latime, inaltime, simbol = "@"):
    print(simbol * latime)
    for i in range(inaltime - 2):
        print(simbol + " " * (latime - 2) + simbol)
    print(simbol* latime)


printeaza_dreptunghi(10, 10)
printeaza_dreptunghi(5, 5)
printeaza_dreptunghi(5, 5, "*")

