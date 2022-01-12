# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("task3_test_file.txt", encoding="UTF-8") as file:
    lines = file.readlines()
    names = []
    salaries_sum = 0
    for line in lines:
        line = line.rstrip('\n')
        name, salary = line.split(', ')
        if int(salary) < 20000:
            names.append(name)
        salaries_sum += int(salary)
    print(f'Средяя величина дохода сотрудников - {salaries_sum / len(lines)}\n')
    print(f'Сотрудники с зарплатой ниже 20000 - {names}')
