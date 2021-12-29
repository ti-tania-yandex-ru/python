# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    return result


dividend = float(input('Введите делимое: '))
divider = float(input('Введите делитель: '))
print(f'Результат деления: {divide(dividend, divider)}')
