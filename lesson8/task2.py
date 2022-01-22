class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


x = int(input('Введите делимое: '))
y = int(input('Введите делитель: '))
z = 0

try:
    if y == 0:
        raise DivisionByZeroError('На ноль делить нельзя!')
except DivisionByZeroError as err:
    print(err)
    z = None
else:
    z = x / y
finally:
    print(f'Рузультат вычислений: {z}')
