
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.


def dz_1_2(a=5, b=6):
    print(f'a & b = {a & b}')
    print(f'a | b = {a | b}')
    print(f'a ^ b = {a ^ b}')
    print(f'~a = {~a}')
    print(f'~b = {~b}')

    print(f'a >> 2 = {a>>2}')
    print(f'a << 2 = {a<<2}')


if __name__ == '__main__':
    dz_1_2()

