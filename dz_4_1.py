
#  Проанализировать скорость и сложность одного любого алгоритма,
#  разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Анализируем 9-е задание из 3-его урока

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import cProfile
import time as t
import random


def dz_3_9_1():
    mas = []
    m = 1000
    n = 1000
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
    # for i in range(m):
    #     print(*mas[i])
    print(f'Максимальный элемент среди минимальных элементов столбцов = {max_el}')


def dz_3_9_2():
    mas = []
    m = 1000
    n = 1000
    for i in range(m):
        b = []
        for j in range(n):
            b.append(random.randint(10, 99))
        mas.append(b)
    b = []
    max_el = 0  # знаем, что числа в матрице только больше нуля
    for j in range(n):
        min_el = mas[0][j]
        for i in range(m):
            if mas[i][j] < min_el:
                min_el = mas[i][j]
        b.append(min_el)
        if min_el > max_el:
            max_el = min_el
    # for i in range(m):
    #     print(*mas[i])
    print(f'Максимальный элемент среди минимальных элементов столбцов = {max_el}')


if __name__ == '__main__':
    time_s = t.time()
    dz_3_9_1()
    time_f = t.time()
    print(time_f - time_s, 'с')

    time_s = t.time()
    dz_3_9_2()
    time_f = t.time()
    print(time_f - time_s, 'с')

# Сложность алгоритма в реализации dz_3_9_1 = O(m x n), где m и n количество строк и столбцов двумерной матрицы.
# Общёт матрицы 1000 х 1000 занимает ~ 1 секунду.
# Функция max(b) добавляет + n к формуле количества условных операций

# Сложность алгоритма dz_3_9_2 аналогично = O(m x n), но уже без + n, поэтому скорость выплнения немногим быстрее.
# Выигрышь скорости получается при условии, если заранее известно число, меньше которого быть не может.




