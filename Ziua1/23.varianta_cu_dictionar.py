"""Creaţi un program în care utilizatorul va insera o sumă întreagă (ex: 128).

Programul trebuie să calculeze şi să afişeze numărul corespunzător de bancnote, unde în program sunt definite bancnotele cu valorile: 10, 5, 2 şi 1"""

total = 128

# bancnote = (10, 5, 2, 1)

bancnote = (100, 50, 10, 5, 1)

calculator = {}

for banc in bancnote:
    nr_bancnote = total // banc
    total = total % banc
    calculator[banc] = nr_bancnote

print(calculator)


