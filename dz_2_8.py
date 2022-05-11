
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def dz_2_8(n, find_n):
    result = 0
    while n > 0:
        while True:
            chek_number = input('Число: ')
            if chek_number.isdigit():
                break
            else:
                print('Введено не число')
        result += chek_number.count(find_n)
        n -= 1
    return result


if __name__ == '__main__':
    print(
        dz_2_8(
            int(input('Количество вводимых чисел: ')),
            input('Искомая цифра: ')
        )
    )
