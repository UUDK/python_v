def _trapez_arr(s1, y2, w):
    return w * (s1 + y2) / 2

def inte(f, a, b, e):
    sum = 0.0
    x1 = a
    x2 = a + e
    y1 = f(x1)
    y2 = f(x2)
    while x2 < b:
        arr = _trapez_arr(y1, y2, e)
        sum += arr
        y1 = y2
        x1 = x2
        x2 = x2 + e
        y2 = f(x2)
    arr = _trapez_arr(y1, f(b), b-x1)
    sum += arr
    return sum

if __name__ == "__main__":
    print(inte(lambda x: 1/(1 + x**2), 0, 3, 1))
    print(inte(lambda x: 1/(1 + x**2), 0, 3, 0.1))
    print(inte(lambda x: 1/(1 + x**2), 0, 3, 0.01))
    print(inte(lambda x: 1/(1 + x**2), 0, 3, 0.001))
