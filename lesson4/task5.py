# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа # от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения
# всех элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce


def mult(prev_el, el):
    return prev_el * el


a = [element for element in range(100, 1001) if element % 2 == 0]

print(a)
print(reduce(mult, a))
