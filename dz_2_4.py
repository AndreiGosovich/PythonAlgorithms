
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def dz_2_4(n):
    current_val = 1
    result = 0
    while n > 0:
        result += current_val
        current_val = current_val / 2 * -1
        n -= 1
    return result


if __name__ == '__main__':
    print(
        dz_2_4(
            int(input('Число элементов: '))
        )
    )
