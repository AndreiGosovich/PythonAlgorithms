
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def dz_1_9(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print('Минимум одно из значений не число')
        exit(1)

    if a > b:
        if a > c:
            if b > c:
                return b
            return c
        return a
    if a > c:
        return a
    if b > c:
        return c
    return b


if __name__ == '__main__':
    print(
        dz_1_9(
            input('a:  '),
            input('b:  '),
            input('c:  ')
        )
    )
