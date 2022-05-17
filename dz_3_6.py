
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random


def dz_3_6():
    mas = list()
    for i in range(10):
        mas.append(random.randint(1, 10))
    print(mas)
    min_el = [mas[0], 0]
    max_el = [mas[0], 0]
    for i in range(1, len(mas)):
        if mas[i] < min_el[0]:
            min_el[0] = mas[i]
            min_el[1] = i
        if mas[i] > max_el[0]:
            max_el[0] = mas[i]
            max_el[1] = i
    print(f'Позиция минимума = {min_el[1]}')
    print(f'Позиция максимума = {max_el[1]}')
    print(f'Сумма элементов между = ', end='')
    if min_el[1] < max_el[1]:
        print(sum(mas[min_el[1] + 1:max_el[1]]))
    else:
        print(sum(mas[max_el[1] + 1:min_el[1]]))


if __name__ == '__main__':
    dz_3_6()
