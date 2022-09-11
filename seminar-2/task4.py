# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input('Ведите количество элементов: '))
arr = [random.randint(-n, n) for i in range(1, n + 1)]
print(arr)

pos_amount = int(input('Ведите количество позиций для перемножения: '))

positions = [f'{random.randint(0, n - 1)}\n' for i in range(pos_amount)]
print(positions)
f = open('positions.txt', 'w')
f.writelines(positions)
f.close()

mult = 1
f = open('positions.txt', 'r')
for line in f:
    mult *= arr[int(line)]
    print(line)
f.close()

print(f'Произведение чисел по позициям: {mult}')
