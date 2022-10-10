from datetime import datetime as dt


def get_log(operation, data):
    time = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{time}: Операция {operation}: {data} \n')
