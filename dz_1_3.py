
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

def dz_1_3(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    if k not in (-1, 0, 1):
        result = f'y = {k:.2g}x'
    elif k == 1:
        result = f'y = x'
    elif k == -1:
        result = f'y = -x'
    else:
        result = f'y ='

    if b > 0:
        return f'y = {b:.2g}' if k == 0 else f'{result} + {b:.2g}'
    elif b < 0:
        return f'{result} {b:.2g}'
    return f'{result} 0' if k == 0 else result


if __name__ == '__main__':
    print(
        dz_1_3(
            int(input('x1 = ')),
            int(input('y1 = ')),
            int(input('x2 = ')),
            int(input('y2 = '))
        )
    )
