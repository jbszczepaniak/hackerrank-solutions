from collections import namedtuple
Date = namedtuple('Date', 'day month year')

def calculate_fine(due_date, ret_date):
    if due_date.year == ret_date.year:
        if due_date.month == ret_date.month:
            if due_date.day >= ret_date.day:
                return 0
            else:
                return (ret_date.day - due_date.day) * 15
        elif due_date.month > ret_date.month:
            return 0
        else:
            return (ret_date.month - due_date.month) * 500
    elif due_date.year > ret_date.year:
        return 0
    else:
        return 10000