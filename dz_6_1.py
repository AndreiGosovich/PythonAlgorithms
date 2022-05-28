
#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#  Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
import random
import sys
# Выбраны задания 5, 7 и 9 из 3 урока.

# Версия Python 3.10.0, 64-разрядная операционная система Windows 10 Pro


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

    print('i = ', sys.getsizeof(i))
    print('max_negative = ', sys.getsizeof(max_negative))
    print('mas = ', sys.getsizeof(mas))


# dz_3_5()
# Сложность алгоритма O(n).
# Простанственная сложность O(1) - выходные данные не зависят от размера обрабатываемого массива.
# Переменные: i = 28 byte, max_negative = 72 byte, mas = 248.


def dz_3_7():
    mas = list()
    for i in range(20):
        mas.append(random.randint(1, 10))
    print(mas)
    minimums = [mas[0], mas[1]]
    for i in range(2, len(mas)):
        if mas[i] < minimums[0]:
            minimums[0] = mas[i]
        elif mas[i] < minimums[1]:
            minimums[1] = mas[i]
    print(minimums)

    print('i = ', sys.getsizeof(i))
    print('minimums = ', sys.getsizeof(minimums))
    print('mas = ', sys.getsizeof(mas))

# dz_3_7()
# Сложность алгоритма O(n).
# Простанственная сложность O(1).
# Переменные: i = 28 byte, minimums = 72 byte, mas = 248.


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

    print('i = ', sys.getsizeof(i))
    print('n = ', sys.getsizeof(m))
    print('m = ', sys.getsizeof(n))
    print('b = ', sys.getsizeof(b))
    print('max_el = ', sys.getsizeof(max_el))
    print('mas = ', sys.getsizeof(mas))


dz_3_9()
# Сложность алгоритма O(n*n).
# Простанственная сложность O(n) - создаётся новый массив размером с количество столбцов.
# Переменные: i = 28, m = 28, n = 28, max_el = 28, mas = 120, b = 88.
# Для оптимизации можно не использовать список b и выполнять сравнение max_el и min_el.
# Массив b, используемый при заполнении входных данных не считаем частью алгоритма задания.

