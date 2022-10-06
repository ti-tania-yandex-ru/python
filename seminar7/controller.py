from interface import input_number
from interface import choose_operation_menu
from interface import choose_numbers_type
import rational
import comlex


def start():
    num_type = choose_numbers_type()
    op = choose_operation_menu()
    x = input_number()
    y = input_number()
    result = None
    if num_type == 1:
        x = float(x)
        y = float(y)
        if op == 1:
            result = rational.add(x, y)
        elif op == 2:
            result = rational.subtract(x, y)
        elif op == 3:
            result = rational.multiply(x, y)
        elif op == 4:
            result = rational.division(x, y)
    elif num_type == 2:
        if op == 1:
            result = comlex.add(x, y)
        elif op == 2:
            result = comlex.subtract(x, y)
        elif op == 3:
            result = comlex.multiply(x, y)
        elif op == 4:
            result = comlex.division(x, y)
    print(f'Результат операции = {result}')
