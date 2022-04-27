
# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def dz_1_8(year):
    if year % 4:
        return f'{year} не високосный'
    if year % 100:
        return f'{year} високосный'
    if year % 400:
        return f'{year} не високосный'
    return f'{year} високосный'


if __name__ == '__main__':
    print(
        dz_1_8(
            int(input("Введите год: "))
        )
    )
