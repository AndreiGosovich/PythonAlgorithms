
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

def dz_2_8():
    max_n = 0
    sum_n = 0
    while True:
        n = input('Число: ')
        if n == '!':
            break
        if sum(int(_) for _ in n) > sum_n:
            sum_n = sum(int(_) for _ in n)
            max_n = n
    if max_n and sum_n:
        print(f'Наибольшее число {max_n}, сумма цифр = {sum_n}')
    else:
        exit(1)


if __name__ == '__main__':
    dz_2_8()