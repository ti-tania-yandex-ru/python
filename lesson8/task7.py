class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        print(f'Результат сложения комплексных чисел = {self.number + other.number}')

    def __mul__(self, other):
        print(f'Результат умножения комплексных чисел = {self.number * other.number}')


num1 = ComplexNumber(2 + 3j)
num2 = ComplexNumber(-1 + 1j)
print(num1 + num2)
print(num1 * num2)

num3 = ComplexNumber(12 - 8j)
num4 = ComplexNumber(-6.1 - 0j)
print(num3 + num4)
print(num3 * num4)
