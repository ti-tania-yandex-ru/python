from logger import log_info

def add(a, b):
    log_info(f'Сложение рациональных чисел {a} и {b}')
    return a + b


def subtract(a, b):
    log_info(f'Вычитание рациональных чисел {a} и {b}')
    return a - b


def multiply(a, b):
    log_info(f'Умножение рациональных чисел {a} и {b}')
    return a * b


def division(a, b):
    log_info(f'Деление рациональных чисел {a} и {b}')
    if b == 0:
        print('Операция деления на ноль недопустима')
        return None
    else:
        return a / b
