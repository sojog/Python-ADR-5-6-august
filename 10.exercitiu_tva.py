"""Creaţi un x care va lua de la utilizator preţul produsului şi va calcula pretul final, cu taxa inclusa.
În cadrul programului este hardcodată taxa la valoarea de 21%.
"""

TVA = 21

while True:

    x = input("Introduceti un numar \n")
    print("Ai introdus:", x)

    x = float(x)
    
    x_cu_tva = x + x * TVA / 100
    print("Pretul cu TVA  este:", x_cu_tva)