
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

def dz_3_1():
    s = set()
    for i in range(2, 100):
        is_multiple = True
        for j in range(2, 10):
            if i % j != 0:
                is_multiple = False
        if is_multiple:
            s.add(i)
    return len(s)


if __name__ == '__main__':
    print(dz_3_1())
