# Convert the module to a package with the three conversions
# in separate files

import convpack

choice = input("Convert what? (f, c, i, m, g, l) : ")
if choice == "f":
    f = input("Enter f : ")
    c = convpack.f2c(float(f))
    print(f"c = {c}")
elif ...:
    ...
else:
    print("Not a correct choice!")
