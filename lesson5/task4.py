# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task4_test_file_input.txt', 'r') as file_input, open('task4_test_file_output.txt', 'w') as file_output:
    final_content = ""
    for line in file_input:
        new_line = ""
        for key in eng_rus_dict:
            index = line.find(key)
            if index != -1:
                new_line = line.replace(key, eng_rus_dict[key])
        final_content += new_line
    file_output.write(final_content)
