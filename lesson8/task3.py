class NonNumberTypeInListError(Exception):
    def __init__(self, message):
        self.message = message


numbers_str = []
numbers = []

while True:
    input_str = input('Введите числo: ')
    if not input_str:
        break
    try:
        number = float(input_str)
        numbers.append(number)
    except ValueError:
        try:
            raise NonNumberTypeInListError("Можно вводить только числа!")
        except NonNumberTypeInListError as e:
            print(e.message)

print(f'Результат: {numbers}')
