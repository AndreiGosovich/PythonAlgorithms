
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
import time


def dz_7_2(mas_float):
    def neumann(mas):
        # разбить на упорядоченные массивы
        sub_mas_list = []
        sub_mas = []
        for i in range(len(mas) - 1):
            if mas[i] <= mas[i + 1]:
                sub_mas.append(mas[i])
            else:
                sub_mas.append(mas[i])
                sub_mas_list.append(sub_mas)
                sub_mas = []
            if i == len(mas) - 2:
                sub_mas.append(mas[i + 1])
                sub_mas_list.append(sub_mas)

        if len(sub_mas_list) > 1:
            # объединить массивы в один
            sub_mas = []
            while True:
                b = None
                if len(sub_mas_list) > 0:
                    a = sub_mas_list[0][0]
                    if len(sub_mas_list) > 1:
                        b = sub_mas_list[1][0]
                    if b is not None:
                        if a <= b:
                            sub_mas.append(a)
                            del(sub_mas_list[0][0])
                        else:
                            sub_mas.append(b)
                            del (sub_mas_list[1][0])
                    else:
                        sub_mas.append(a)
                        del (sub_mas_list[0][0])
                    if len(sub_mas_list[0]) == 0:
                        del(sub_mas_list[0])
                    if len(sub_mas_list) > 1 and len(sub_mas_list[1]) == 0:
                        del(sub_mas_list[1])
                else:
                    break
            # вызывать рекурсивную функцию
            return neumann(sub_mas)
        else:
            return mas
    return neumann(mas_float)


if __name__ == '__main__':
    mas = []
    for _ in range(100):
        mas.append(random.uniform(0, 50))
        # mas.append(random.randint(0, 50))
    print(mas)
    print(dz_7_2(mas))

# Сложность алгоритма O(n*n)
# Пространственная сложность O(n*n)
