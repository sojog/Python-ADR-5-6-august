
# a, b - obligatoriu, args - optional
def functia_mea(a, b, *args, **kargs):
    print(a, b)
    print(args, type(args))
    print(kargs, type(kargs))

functia_mea(10, 2)
functia_mea(10, 2, 20, 30, 40)

functia_mea(10, 2, x=20, y=30, z=40)


functia_mea(10, 2, 300, 400,  x=20, y=30, z=40)