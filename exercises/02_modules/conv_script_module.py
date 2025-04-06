# (Create a module that can convert between Celsius and Fahrenheit,
#           inches and millimeters, and gallon and liters)
# Create a script that uses the functions in the module


import convert

choice = input("Convert what? (f, c, i, m, g, l) : ")
if choice == "f":
    f = input("Enter f : ")
    c = convert.f2c(float(f))
    print(f"c = {c}")
elif ...:
    ...
else:
    print("Not a correct choice!")
