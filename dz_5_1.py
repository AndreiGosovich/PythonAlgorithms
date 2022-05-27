
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections


def dz_5_1():
    companies = {}
    for i in range(int(input('Количество предприятий: '))):
        company_name = input(f'Название предприятия № {i + 1}: ')
        companies[company_name] = sum([
            int(input('Прибыль за первый квартал: ')),
            int(input('Прибыль за второй квартал: ')),
            int(input('Прибыль за третий квартал: ')),
            int(input('Прибыль за четвёртый квартал: '))
        ])
    companies = collections.Counter(companies)
    avg_profit = companies.total() / len(companies)
    print(f'Средняя прибыль предприятий: {avg_profit}')
    print('Предприятия с прибылью выше среднего:')
    for company, profit in companies.items():
        if profit > avg_profit:
            print(f'    {company}')
    print('Предприятия с прибылью ниже среднего:')
    for company, profit in companies.items():
        if profit < avg_profit:
            print(f'    {company}')


if __name__ == '__main__':
    dz_5_1()

# Сложность алгоритма O(n).
# Выполнение алгоритма расчёта и вывода данных скорее всего будет намного быстрее скорости ввода данных пользователем.
