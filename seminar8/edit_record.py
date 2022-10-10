from tempfile import NamedTemporaryFile
import shutil
import csv

file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Номер_телефона', ]


def edit_record(id, new_dict):
    tempfile = NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
    with open('phonebook.csv', 'r', encoding='utf-8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=file_headers)
        writer = csv.DictWriter(tempfile, fieldnames=file_headers)
        for row in reader:
            if row['id'] == str(id):
                row['Фамилия'], row['Имя'], row['Отчество'], row['Номер_телефона'] = new_dict['Фамилия'], new_dict[
                    'Имя'], new_dict['Отчество'], new_dict['Номер_телефона']
            row = {'id': row['id'], 'Фамилия': row['Фамилия'], 'Имя': row['Имя'], 'Отчество': row['Отчество'],
                   'Номер_телефона': row['Номер_телефона']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'phonebook.csv')
