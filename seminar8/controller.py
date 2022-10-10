from interface import get_dict, get_element, get_choice, get_search_criteria
from add_record import add_record
from search_record import search
from logger import get_log
from edit_record import edit_record


def push_rocket():
    operation_num = get_choice()
    if operation_num == 1:
        new_dict = get_dict()
        add_record(new_dict)
        get_log('Добавление данных', new_dict)
    elif operation_num == 2:
        search_criteria = get_search_criteria()
        search(search_criteria)
        get_log('Поиск данных', search_criteria)
    elif operation_num == 3:
        search_criteria = get_search_criteria()
        search(search_criteria)
        index = get_element()
        new_dict = get_dict()
        edit_record(index, new_dict)
        get_log('Редактирование данных', new_dict)
