
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def dz_2_7(n):
    result = sum(int(_) for _ in range(n + 1)) == n * (n + 1) / 2
    if n > 0 and result:
        n -= 1
        result = dz_2_7(n)
    return result


if __name__ == '__main__':
    print(
        dz_2_7(
            int(input('Число: '))
        )
    )
