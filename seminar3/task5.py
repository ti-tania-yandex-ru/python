# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#     Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = 0
fib2 = 1

n = int(input('Введите число: '))

fibonacci = [fib1, fib2]

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    fibonacci.append(fib2)
print(fibonacci)

negative_fibonacci = []
for i in range(1, len(fibonacci)):
    if not (i % 2):
        negative_fibonacci.append(fibonacci[i] * (-1))
    else:
        negative_fibonacci.append(fibonacci[i])

negative_fibonacci = negative_fibonacci[::-1]
print(negative_fibonacci + fibonacci)
