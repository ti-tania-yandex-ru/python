#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
#     Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

# старый вариант решения -

number = input('Введите число: ')
summa = 0
for num in number:
    if num != ',':
        summa += int(num)
print(f'Сумма цифр равна {summa}')

# Новое решение с использованием filter и map

print(f'Сумма цифр равна {sum(map(int, filter(lambda numb: numb != ",", number)))}')
