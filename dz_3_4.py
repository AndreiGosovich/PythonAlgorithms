
# Определить, какое число в массиве встречается чаще всего
import random


def dz_3_4():
    mas = list()
    for i in range(20):
        mas.append(random.randint(1, 10))
    max_count = [0, 0]
    for i in range(len(mas)):
        tmp_count = mas.count(mas[i])
        if tmp_count > max_count[0]:
            max_count[0] = tmp_count
            max_count[1] = mas[i]
    print(mas)
    print(f'Чаще всего встречается число {max_count[1]}, повторов {max_count[0]}')


if __name__ == '__main__':
    dz_3_4()
