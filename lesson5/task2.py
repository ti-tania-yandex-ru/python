# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open("task2_test_file.txt", 'r')

lines = file.readlines()
print(f'Количество строк в файле - {len(lines)} \n')

file.seek(0)
i = 1

for line in file:
    print(line)
    words = line.split(' ')
    print(f'Количетво слов в строке {i} - {len(words)} \n')
    i += 1

file.close()
