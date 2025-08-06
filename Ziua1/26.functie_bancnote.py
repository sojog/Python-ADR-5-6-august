

# definitia functiei
def calculeaza_bancnote(total):    
    bancnote = (100, 50, 10, 5, 1)

    calculator = {}

    for banc in bancnote:
        nr_bancnote = total // banc
        total = total % banc
        calculator[banc] = nr_bancnote

    print(calculator)


# apeleaza functiei
calculeaza_bancnote(128)


# apeleaza functiei
calculeaza_bancnote(197)


# apeleaza functiei
calculeaza_bancnote(300)