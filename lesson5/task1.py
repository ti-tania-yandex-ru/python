# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

out_f = open("task1_test_file.txt", "w")

while True:
    new_line = input("Введите строку файла: ")
    if new_line != '':
        out_f.write(f'{new_line}\n')
    else:
        break

out_f.close()
