

## Versiunea 1 (mai veche) -  CITITRE DIN FISIER
file_handler = open("valori.txt", "r")
text_citit = file_handler.read()
file_handler.close()
print(text_citit)


## Versiunea 2 (mai nou / preferata) - CITITRE DIN FISIER

with open("valori.txt", "r") as file_handler:
    text_citit = file_handler.read()
print(text_citit)