
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться
import random


def dz_3_7():
    mas = list()
    for i in range(10):
        mas.append(random.randint(1, 10))
    print(mas)
    minimums = [mas[0], mas[1]]
    for i in range(2, len(mas)):
        if mas[i] < minimums[0]:
            minimums[0] = mas[i]
        elif mas[i] < minimums[1]:
            minimums[1] = mas[i]
    print(minimums)


if __name__ == '__main__':
    dz_3_7()
