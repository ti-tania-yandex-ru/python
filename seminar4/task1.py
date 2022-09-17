# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. *Сохранить словарь в файл users_hobby.txt.
# Фрагмент файла с данными о пользователях (users.txt): Иванов Иван Иванович Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt): скалолазание, охота горные лыжи

users_hobby = {}

with open('users.txt', encoding='utf8') as users, open('hobby.txt', encoding='utf8') as hobby:
    for line1, line2 in zip(users, hobby):
        line1 = line1.strip('\n')
        line2 = line2.strip('\n')
        users_hobby[line1] = line2
with open('users_hobby.txt', 'w', encoding='utf8') as users__hobby:
    users__hobby.write(str(users_hobby))
