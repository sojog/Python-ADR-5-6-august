"""Creaţi un program în care utilizatorul va insera o sumă întreagă (ex: 128).

Programul trebuie să calculeze şi să afişeze numărul corespunzător de bancnote, unde în program sunt definite bancnotele cu valorile: 10, 5, 2 şi 1"""

total = 128

bancnote = [10, 5, 2, 1]

for banc in bancnote:

    nr_bancnote = total // banc
    print("bancnote de ", banc, "este:" , nr_bancnote)

    total = total % banc
    print("restul dupa impartirea la banc:", total)