import csv

# Versiunea 1 - clasica
with open("valori.csv", "r") as freader:
    continut = freader.read() 
    print(continut, type(continut))


# Versiunea 2 - cea cu modulul csv
with open("valori.csv", "r") as freader:
    csv_reader = csv.reader(freader)
    print(csv_reader)
    for row in csv_reader:
        print(row, type(row))