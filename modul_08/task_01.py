"""
Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів 
від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).
"""

from datetime import datetime


def get_days_from_today(date: str):
    current_datetime = datetime.now().date()

    date = list(map(int, date.split('-')))

    date = datetime(year=date[0], month=date[1], day=date[2]).date()

    delta_time = current_datetime - date
    
    return int(delta_time.total_seconds()/ (60 * 60 *24))

print(get_days_from_today('2020-10-09'))