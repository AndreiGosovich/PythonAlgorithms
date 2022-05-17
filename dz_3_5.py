
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random


def dz_3_5():
    mas = list()
    for i in range(20):
        mas.append(random.randint(-20, 10))
    max_negative = [mas[0], 0]
    for i in range(1, len(mas)):
        if mas[i] < 0 and (mas[i] > max_negative[0] or max_negative[0] >= 0):
            max_negative[0] = mas[i]
            max_negative[1] = i
    print(mas)
    print(f'Максимальный отрицательный элемент {max_negative[0]}, позиция {max_negative[1]}')


if __name__ == '__main__':
    dz_3_5()
