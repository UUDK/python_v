# Create a module that can convert between Celsius and Fahrenheit,
# inches and millimeters, and gallon and liters


def f2c(f):
    return (f - 32) * 5 / 9


def c2f(c):
    return (c * 9 / 5) + 32


def i2m(i):
    return i * 25.4


def m2i(m):
    return m / 25.4


def g2l(g):
    return g * 3.8


def l2g(l):  # noqa: E741
    return l / 3.8
