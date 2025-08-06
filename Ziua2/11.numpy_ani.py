
import numpy as np

start_year = input("Introduceti anul de inceput ")
while not start_year.isnumeric():
    start_year = input("Introducet un numar pentru anul de inceput ")


stop_year = input("Introduceti anul de final ")
while not stop_year.isnumeric():
    stop_year = input("Introducet un numar pentru anul de final ")

start_year =  int(start_year)
stop_year = int(stop_year)


all_years = np.arange(start_year, stop_year + 1)

conditie1 = all_years % 400 == 0
conditie2 = (all_years % 100 != 0) & (all_years % 4 == 0)

leap_years = all_years[ conditie1 | conditie2]
print(leap_years)


