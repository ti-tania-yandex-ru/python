import csv

file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Номер_телефона', ]


def add_record(user_dict):
    global file_headers
    with open('phonebook.csv', 'r', encoding='utf-8') as csvfile:
        index = 0
        reader = csv.DictReader(csvfile)
        for row in reader:
            if index < int(row['id']):
                index = int(row['id'])

    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=file_headers)
        csv_writer.writerow({'id': index + 1, 'Фамилия': user_dict['Фамилия'],
                             'Имя': user_dict['Имя'],
                             'Отчество': user_dict['Отчество'],
                             'Номер_телефона': user_dict['Номер_телефона']})
