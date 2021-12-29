# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.
# СПЕЦ-СИМВОЛ - знак !

def parse_string_and_get_sum(my_str):
    my_list = my_str.split()
    final_list = []
    is_special_symbol_found = False
    for x in my_list:
        if x != '!':
            final_list.append(x)
        else:
            is_special_symbol_found = True
            break
    final_list = [int(x) for x in final_list]
    return sum(final_list), is_special_symbol_found


total_sum = 0

while True:
    input_str = input('Введите числа, разделив пробелом: ')
    summ, symbol_found = parse_string_and_get_sum(input_str)
    total_sum = total_sum + summ
    print(f'Общая сумма равна {total_sum}')
    if symbol_found:
        break
