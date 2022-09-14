# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
#     Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal

numbers = [1.1, 1.2, 3.1, 5, 10.01, 11.003]
fraction_numbers = []

# Удалим те числа, у которых нет дробной части:
for num in numbers:
    if str(num).find('.') == -1:
        numbers.remove(num)

# От каждого числа отнимем целую часть, чтобы в новом массиве остались только дробные, а целая часть была равна 0.
# Используем Decimal чтобы избежать странного результата при вычитании
for num in numbers:
    fraction_numbers.append(Decimal(str(num)) - Decimal(int(num)))

print(max(fraction_numbers) - min(fraction_numbers))
