
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа
import random


def dz_3_2():
    mas = list()
    for i in range(20):
        mas.append(random.randint(1, 1000))
    mas_even = list()
    for i in range(len(mas)):
        if not mas[i] % 2:
            mas_even.append(i)
    print(mas)
    print(mas_even)


if __name__ == '__main__':
    dz_3_2()
