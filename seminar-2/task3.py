#     Задайте список из n чисел последовательности (1+1\n)^n и выведите на экран их сумму.
#
#     Пример:
#
# - Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

num = int(input('Ведите число: '))
numbers = []
for i in range(1, num + 1):
    numbers.append((1 + 1 / i) ** i)
print(numbers)
print(f'Общая сумма: {sum(numbers)}')
