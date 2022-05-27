
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections
import time


class HexNumber:
    def __init__(self, hex_number):
        self.alphabet = collections.UserList('0123456789ABCDEF')
        hex_number = collections.UserList(hex_number.upper())
        if set(hex_number).issubset(set(self.alphabet)):
            self.hex_number = hex_number
        else:
            raise Exception('Введены неверные значения!')

    def __str__(self):
        return str(self.hex_number)

    def __add__(self, other):
        a_hex = self.hex_number
        b_hex = other.hex_number
        result = collections.deque('')
        one = 0
        i = 1
        n = max(len(a_hex), len(b_hex))
        while i <= n:
            a_10 = 0
            b_10 = 0
            if len(a_hex) >= i:
                a_10 = self.alphabet.index(a_hex[len(a_hex) - i])
            if len(b_hex) >= i:
                b_10 = self.alphabet.index(b_hex[len(b_hex) - i])
            s = a_10 + b_10 + one
            if s >= 16:
                s = s - 16
                one = 1
                if i == n:
                    n += 1
            else:
                one = 0
            result.appendleft(self.alphabet[s])
            i += 1
        return HexNumber(''.join(result))

    def __mul__(self, other):
        if len(self.hex_number) > len(other.hex_number):
            a_hex = other.hex_number
            b_hex = self.hex_number
        else:
            a_hex = self.hex_number
            b_hex = other.hex_number
        result = HexNumber('')
        for i in range(1, min(len(a_hex), len(b_hex)) + 1):
            one = 0
            tmp = collections.deque('0' * (i - 1))
            for j in range(1, max(len(a_hex), len(b_hex)) + 1):
                a_10 = self.alphabet.index(a_hex[len(a_hex) - i])
                b_10 = self.alphabet.index(b_hex[len(b_hex) - j])
                mul = a_10 * b_10 + one
                if mul > 15:
                    one = mul // 16
                    mul = mul - 16 * one
                else:
                    one = 0
                tmp.appendleft(self.alphabet[mul])
            if one:
                tmp.appendleft(str(one))
            result += HexNumber(''.join(tmp))
        return result


if __name__ == '__main__':
    a = HexNumber(input('a = '))
    b = HexNumber(input('b = '))
    t_s = time.time()
    print('a + b = ', a + b)
    print(time.time() - t_s, ', c')
    t_s = time.time()
    print('a * b =', a * b)
    print(time.time() - t_s, ', c')

# Сложность алгорима сложения O(n)
# Сложность алгоритма умножения O(n*n)
# Время выоплнения алгоритмов даже для больших чисел доли секунды.
