# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

with open('task7_test_file.txt', 'r', encoding='utf-8') as file, open("task7_test_file.json", "w") as write_file:
    firms_dict = {}
    average_profit_dict = {}
    firms_amount = 0
    total_profit = 0
    for line in file:
        firm_data = line.split(' ')
        firm_name = firm_data[0]
        firm_proceeds = int(firm_data[2])
        firm_costs = int(firm_data[3])
        firm_profit = firm_proceeds - firm_costs
        if firm_profit > 0:
            total_profit += firm_profit
            firms_amount += 1
        firms_dict[firm_name] = firm_profit
    average_profit_dict["average profit"] = total_profit / firms_amount
    data_list = [firms_dict, average_profit_dict]
    print(data_list)
    json.dump(data_list, write_file)
