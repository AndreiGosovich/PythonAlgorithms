
#  Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
import time as t


def sieve(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m]:
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1
    # for i in a:
    #     if a[i]:
    #         print(a[i], end=' ')
    # print('')


def dz_4_2(n):
    b = []
    for i in range(2, n + 1):
        is_natural = True
        for j in range(2, i):
            if i % j == 0:
                is_natural = False
                break
        if is_natural:
            b.append(i)
    # print(*b)


if __name__ == '__main__':
    n = 10000
    t_s = t.time()
    sieve(n)
    t_f = t.time()
    print(f'Решето Эратосфена = {t_f - t_s}, секунд')
    t_s = t.time()
    dz_4_2(n)
    t_f = t.time()
    print(f'Перебор = {t_f - t_s}, секунд')

# Сложность алгоритма "Решето Эратосфена" O(n * log(log(n))), при n = 10000 время выполнения ~ 0.004 секунды.
# Сложность реализации перебором O(n * n/2), при n = 10000 время выполнения ~ 0.384 секунды.
