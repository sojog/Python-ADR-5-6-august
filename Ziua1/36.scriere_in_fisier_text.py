
print("Introdu 10 numere")

numere = []
for i in range(10):
    nr = input(f"Introdu numarul {i+1}\n")
    numere.append(nr)

print(numere)

with open("numere.txt", "w") as file_writer:
    for nr in numere:
        file_writer.write(nr)
        file_writer.write("\n")