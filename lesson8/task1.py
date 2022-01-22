class Date:
    date_to_format = ""
    day = 0
    month = 0
    year = 0

    def __init__(self, date):
        Date.date_to_format = date

    @classmethod
    def format_to_number(cls):
        data = cls.date_to_format.split('-')
        Date.day = int(data[0])
        Date.month = int(data[1])
        Date.year = int(data[2])

    @staticmethod
    def validate_date():
        if Date.month < 0 or Date.month > 12:
            print(f'Invalid month value.')
        elif Date.day < 0 or (Date.day > 28 and Date.month == 2) or (
                Date.day > 30 and Date.month in (4, 6, 9, 11)) or Date.day > 31:
            print(f'Invalid day value.')
        else:
            print('All is good')


Date('31-13-2001')
Date.format_to_number()
Date.validate_date()
