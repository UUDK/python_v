# (Create a module that can convert between Celsius and Fahrenheit,
#           inches and millimeters, and gallon and liters)
# Create a script that uses the functions in the module


import convert

choice = input("Convert what? (f, c, i, m, g, l) : ")
if choice == "f":
    f = input("Enter f : ")
    c = convert.f2c(float(f))
    print(f"c = {c}")
elif choice == "c":
    c = input("Enter c : ")
    f = convert.c2f(float(c))
    print(f"f = {f}")
elif choice == "i":
    i = input("Enter i : ")
    m = convert.i2m(float(i))
    print(f"m = {m}")
elif choice == "m":
    m = input("Enter m : ")
    i = convert.m2i(float(m))
    print(f"i = {i}")
elif choice == "g":
    g = input("Enter g : ")
    l = convert.g2l(float(g))  # noqa: E741
    print(f"l = {l}")
elif choice == "l":
    l = input("Enter l : ")  # noqa: E741
    g = convert.l2g(float(l))
    print(f"g = {g}")
else:
    print("Not a correct choice!")
