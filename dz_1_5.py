
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def dz_1_5(char_a, char_b):
    if char_a.isalpha() and char_b.isalpha() and len(char_a) == len(char_b) == 1:
        if ord(char_a) in range(ord('a'), ord('y') + 1) and ord(char_b) in range(ord('a'), ord('y') + 1):
            return f'Позиция буквы {char_a} = {ord(char_a) - 96}\nПозиция буквы {char_b} = {ord(char_b) - 96}' \
                   f'\nМежду ними букв = {abs(ord(char_b) - ord(char_a)) - 1}'
        else:
            print('Введено неверное значение')
            exit(1)
    else:
        print('Введено неверное значение')
        exit(1)


if __name__ == '__main__':
    print(dz_1_5(
        input('Первая буква: '),
        input('Вторая буква: ')
    ))
