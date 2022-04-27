
# Написать программу, которая генерирует в указанных пользователем границах:
#   случайное целое число;
#   случайное вещественное число;
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


def dz_1_4(b, e):
    if b.isalpha() and e.isalpha():
        if len(b) == len(e) == 1:
            return chr(random.randint(ord(b), ord(e))) if ord(b) <= ord(e) else chr(random.randint(ord(e), ord(b)))
        else:
            print('Введено неверное значение')
            exit(1)
    elif b.isdigit() and e.isdigit():
        result = random.randint(int(b), int(e)) if int(b) <= int(e) else random.randint(int(e), int(b))
        return result

    try:
        float(b)
        float(e)
        return random.uniform(float(b), float(e))
    except ValueError:
        print('Введено неверное значение')
        exit(1)


if __name__ == '__main__':
    print(dz_1_4(
        input('Начало диапазона: '),
        input('Конец диапазона: ')
    ))
