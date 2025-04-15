def get_min(x, y) :
    return x if x < y else y

print(get_min(3, 5))


def func_exam(a, b) :
    c = a + b
    d = a - b

    return (c, d)

k, l = func_exam(7, 3)

print(k, l)