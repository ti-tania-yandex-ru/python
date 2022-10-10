import csv


def search(search_criteria):
    flag = 1
    with open('phonebook.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if search_criteria in row:
                flag = 0
                print(row)
    if flag:
        print('Не найден в справочнике')
