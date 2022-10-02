# Напишите программу, которая найдёт произведение пар чисел списка.
#     Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#     Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# -- старый вариант решения -

numbers = [1, 2, 8, 4, -1, 9, 0, 3, 4, 6, 3]
result = []

i_range = 0
if len(numbers) % 2:
    i_range = 1

for i in range(len(numbers) // 2 + i_range):
    result.append(numbers[i] * numbers[-1 * (i + 1)])
print(f'Произведение пар чисел списка: \n {result}')

# Новое решение с использованием list comprehension

print(f'Произведение пар чисел списка: \n '
      f'{[numbers[i] * numbers[-1 * (i + 1)] for i in range(len(numbers) // 2 + i_range)]}')
