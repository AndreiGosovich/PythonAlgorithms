
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


def dz_3_9():
    mas = []
    m = 5
    n = 4
    for i in range(m):
        b = []
        for j in range(n):
            b.append(random.randint(10, 99))
        mas.append(b)
    b = []
    max_el = 0
    for j in range(n):
        min_el = mas[0][j]
        for i in range(m):
            if mas[i][j] < min_el:
                min_el = mas[i][j]
        b.append(min_el)
        max_el = max(b)
    for i in range(m):
        print(*mas[i])
    print(f'Максимальный элемент среди минимальных элементов столбцов = {max_el}')


if __name__ == '__main__':
    dz_3_9()
