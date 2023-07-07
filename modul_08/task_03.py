""""
Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі 
ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 'Thursday 27 May 2021' - 
день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.
"""
from datetime import datetime


def get_str_date(date):
#     date = list(map(int, date.split(' ')[0].split('-')))
#     date = datetime(year=date[0], month=date[1], day=date[2])
#     return date.strftime('%A %d %B %Y')

    date = datetime.fromisoformat(date[:-1])
    return date.strftime('%A %d %B %Y')


print(get_str_date('2021-05-27 17:08:34.149Z'))