from datetime import datetime


def log_info(user, operation):
    with open('log.txt', 'a', encoding='utf-8') as logfile:
        logfile.write(f'{datetime.now()}: {user}, {operation}\n')
