number = input('Введите положительное целое число: ')
i = 0
max_number = 0

while i < len(number):
    if int(number[i]) > max_number:
        max_number = int(number[i])
    i += 1

print(f'Максимальное число: {max_number}')
