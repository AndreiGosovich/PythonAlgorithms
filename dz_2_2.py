
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

def dz_2_2(n):
    if n.isdigit():
        count_even = 0
        count_odd = 0
        for i in range(0, len(n)):
            if int(n[i]) % 2:
                count_odd += 1
            else:
                count_even += 1
        return f'Чётных цифр: {count_even}\nНечётных цифр: {count_odd}'
    return 'Ошибка ввода'


if __name__ == '__main__':
    print(
        dz_2_2(
            input('Введите число: ')
        )
    )
