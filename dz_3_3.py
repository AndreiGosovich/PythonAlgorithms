
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random


def dz_3_3():
    mas = list()
    for i in range(20):
        mas.append(random.randint(1, 1000))
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
    mas[min_el[1]] = max_el[0]
    mas[max_el[1]] = min_el[0]
    print(mas)


if __name__ == '__main__':
    dz_3_3()
