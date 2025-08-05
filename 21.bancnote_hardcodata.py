"""Creaţi un program în care utilizatorul va insera o sumă întreagă (ex: 128).

Programul trebuie să calculeze şi să afişeze numărul corespunzător de bancnote, unde în program sunt definite bancnotele cu valorile: 10, 5, 2 şi 1"""

total = 128


nr_bancnote_de_10 = total // 10
print("bancnote de 10:", nr_bancnote_de_10)

restul_dupa_10 = total % 10
print("restul dupa impartirea la 10:", restul_dupa_10)



nr_bancnote_de_5 =  restul_dupa_10 // 5
print("bancnote de 5:", nr_bancnote_de_5)

restul_dupa_5 = restul_dupa_10 % 5
print("restul dupa impartirea la 5:", restul_dupa_5)



nr_bancnote_de_2 =  restul_dupa_5 // 2
print("bancnote de 2:", nr_bancnote_de_2)


restul_dupa_2 = restul_dupa_5 % 2
print("restul dupa impartirea la 2:", restul_dupa_2)



nr_bancnote_de_1=  restul_dupa_2 // 1
print("bancnote de 1:", nr_bancnote_de_1)