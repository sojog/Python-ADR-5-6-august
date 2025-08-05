
# 10 - 20 - 30 - 40

# \n -> new line
x = input("Introduceti un numar\n")
print("Ai introdus:", x, type(x))

x  = int(x)

### Versiunea 1 -> imbricata (nu este recomandata)
if x < 10:
    print("Este mai mic ca 10")
else:
    print("Este mai mare sau egal cu 10")
    if x < 20:
        print("Este mai mic ca 20")
    else:
        print("Este mai mare sau egal cu 20")
        if x < 30:
            print("Este mai mic ca 30")
        else:
            print("Este mai mare sau egal cu 30")
            if x < 40:
                print("Este mai mic ca 40")
            else:
                print("Este mai mare ca 40")


# Versiunea 2 - versiunea preferata
if x < 10:
    print("Este mai mic ca 10")
elif x < 20:
    print("Este mai mare sau egal cu 10")
    print("Este mai mic ca 20")
elif x < 30:
    print("Este mai mare sau egal cu 20")
    print("Este mai mic ca 30")
elif x < 40:
    print("Este mai mic ca 40")
else:
    print("Este mai mare sau egal cu 30")
    print("Este mai mare ca 40")