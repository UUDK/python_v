# Create a function that can calculate numeric integration.
# It should take four parameters:
#  the function f,
#  lower limit a,
#  upper limit b, and
#  the width of the segments e


def _trapez_arr(y1, y2, w):
    return w * (y1 + y2) / 2


def inte(f, a, b, e):
    sum = 0.0
    x1 = a
    x2 = a + e
    y1 = f(x1)
    y2 = f(x2)
    ...
    return sum


if __name__ == "__main__":
    prev = 0
    for i in range(8):
        e = 10 ** (-i)
        f = lambda x: 1 / (1 + x**2)  # noqa: E731
        arr = inte(f, -4.1, 4.3, e)
        diff = prev - arr
        print(f"{e=:20.17f}, {arr=:20.17f} {diff=:20.17f}")
        prev = arr
