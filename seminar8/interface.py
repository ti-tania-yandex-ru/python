# функция выбора операции
# 1 - добавить
# 2 - поиск
# 3 - редактировать

def get_choice():
    return int(input('Введите номер операции (1-добавить; 2-поиск; 3-редактировать): '))


def get_element():
    return input('Введите элемент для редактирования: ')


def get_search_criteria():
    return input('Введите данные для поиска: ')


def get_dict():
    keys = ['Фамилия', 'Имя', 'Отчество', 'Номер_телефона', ]
    user_dict = {}
    for i in range(4):
        user_dict[keys[i]] = input(f'Введите {keys[i]} - ')
    return user_dict
