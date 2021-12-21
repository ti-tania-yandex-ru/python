proceeds = int(input('Введите значение выручки фирмы (в долларах): '))
expenses = int(input('Введите значение издержек фирмы (в долларах): '))

if proceeds > expenses:
    print('Фирма работает с прибылью! ')
    print(f'Рентабельность: {proceeds / expenses}')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника: {(proceeds - expenses) / employees} долларов')
else:
    print('Фирма работает в убыток!')
