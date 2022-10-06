from logger import log_info


def add(a, b):
    log_info(f'Сложение комплексных чисел {a} и {b}')
    return complex(a) + complex(b)


def subtract(a, b):
    log_info(f'Вычитание комплексных чисел {a} и {b}')
    return complex(a) - complex(b)


def multiply(a, b):
    log_info(f'Умножение комплексных чисел {a} и {b}')
    return complex(a) * complex(b)


def division(a, b):
    log_info(f'Деление комплексных чисел {a} и {b}')
    b_compl = complex(b)
    if b_compl.real == 0 and b_compl.imag == 0:
        print('Операция деления на ноль недопустима')
        return None
    else:
        return complex(a) / b_compl
