
#  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def dz_1_1(n):
    if not n.isdigit():
        raise Exception(f'{n} - не число')

    if len(n) != 3:
        raise Exception(f'{n} - не трёхзначное число')

    return int(n[0]) + int(n[1]) + int(n[2]), int(n[0]) * int(n[1]) * int(n[2])


if __name__ == '__main__':
    res = dz_1_1(input('Введите трёхзначное число: '))
    print(f'Сумма = {res[0]}\nПроизведение = {res[1]}')
