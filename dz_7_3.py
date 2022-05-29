
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def dz_7_3(mas):
    center = int(len(mas) / 2)

    is_the_end = False
    while not is_the_end:
        is_the_end = True
        for i in range(len(mas)):
            if i < center:
                if mas[i] > mas[center]:
                    mas[center], mas[i] = mas[i], mas[center]
                    is_the_end = False
            else:
                if mas[i] < mas[center]:
                    mas[center], mas[i] = mas[i], mas[center]
                    is_the_end = False
    return mas[center]


if __name__ == '__main__':
    mas = []
    m = 10
    for _ in range(2 * m + 1):
        mas.append(random.randint(1, 100))

    print(mas)
    print('Медиана = ', dz_7_3(mas))

# Сложность алгоритма O(n*n)
# Пространственная сложность O(1)
