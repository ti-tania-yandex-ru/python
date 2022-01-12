# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

numbers = []
n = int(input("Введите количество чисел в файле: "))
for j in range(n):
    numbers.append(random.randint(1, 10))

file_str = ' '.join(str(number) for number in numbers)
print(file_str)

with open('task5_test_file.txt', 'w+') as file_input:
    file_input.write(file_str)
    file_input.seek(0)
    new_str = file_input.read()
    new_numbers = new_str.split(' ')
    new_numbers = [int(i) for i in new_numbers]
    print(f'Сумма элементов списка равна {sum(new_numbers)}')
