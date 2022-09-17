# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

mno = []
counter = 2
n = int(input('Введите натуральное число N: '))

while n > 1:
    if n % counter == 0:
        mno.append(counter)
        n = n // counter
    else:
        counter += 1

print(mno)
