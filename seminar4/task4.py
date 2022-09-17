# *Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

import random

str1 = ''
k = int(input('Задайте степень многочлена: '))
for i in range(0, k + 1):
    koeff = random.randint(0, 10)
    if koeff > 0:
        str1 += '+ '
        if k - i > 1:
            if koeff == 1:
                koeff = ''
            str1 += f'{koeff}x^{k - i} '
        elif k - i == 1:
            if koeff == 1:
                koeff = ''
            str1 += f'{koeff}x '
        else:
            str1 += f'{koeff} '
str1 += '= 0'
str1 = str1.strip('+ ')
print(str1)

with open('mnogochlen.txt', 'w', encoding='utf8') as mnogochlen:
    mnogochlen.write(str1)
