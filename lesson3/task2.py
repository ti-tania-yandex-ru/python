# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_user_data(name, surname, year, city, email, phone):
    print(f'Данные: имя - {name}, фамилия - {surname}, год рождения - {year}, '
          f'город проживания - {city}, email - {email}, телефон - {phone}.')


get_user_data(name='Петя', surname='Птичкин', year='1966', city='Чикаго', email='petya.pt@y.us', phone='123-456-7777')
get_user_data(email='leo.d@yandex.ru', phone='123-456-7777', name='Leo', surname='DiCaprio', year='1977',
              city='Minneapolis')


