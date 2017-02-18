from collections import namedtuple
Date = namedtuple('Date', 'day month year')

def calculate_fine(due_date, ret_day):
    if due_date.year > ret_day.year:
        if due_date.month >= ret_day.month:
            if due_date.day >= ret_day.day:
                return 0
