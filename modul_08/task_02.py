from datetime import datetime, timedelta


def get_days_in_month(month, year, day=1):
    start_date = datetime(year=year, month=month, day=day)
    if month == 12:
        year += 1
        month = 0
    end_date = datetime(year=year, month=month+1, day=day)
    days = end_date - start_date
    return int(days.total_seconds()/ (60 * 60 *24))

print(get_days_in_month(3, 2021))




"""Звичайно, ось кілька прикладів використання .replace() для зміни різних 
частин дати в об'єкті datetime:

Заміна року на 2024:
python"""
from datetime import datetime

date = datetime(2023, 4, 3)
new_date = date.replace(year=2024)
print(new_date)  # 2024-04-03 00:00:00
"""У цьому прикладі ми створили об'єкт date з датою 3 квітня 2023 року, а потім за 
допомогою методу .replace() змінили рік на 2024. Після цього new_date містить дату 3 квітня 2024 року.

Заміна години на 9:
python"""
from datetime import datetime

date = datetime(2023, 4, 3, 8, 30, 0)
new_date = date.replace(hour=9)
print(new_date)  # 2023-04-03 09:30:00
"""У цьому прикладі ми створили об'єкт date з датою 3 квітня 2023 року та часом 8:30 
ранку, а потім за допомогою методу .replace() змінили годину на 9. Після цього new_date 
містить дату 3 квітня 2023 року та час 9:30 ранку.

Заміна дня на останній день місяця:
python"""


from datetime import datetime, timedelta

date = datetime(2023, 4, 3)
last_day = (date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
print(last_day)  # 2023-04-30 00:00:00
"""У цьому прикладі ми використовуємо .replace() для заміни дня на останній день місяця, 
під час визначення дати останнього дня місяця у функції days_in_month(), про яку ми 
говорили раніше. Знову ж таки, ми спочатку додаємо 32 дні до початкової дати, щоб переконатися, 
що ми перевищуємо поточний місяць, а потім замінюємо день на 1, щоб перейти на перший день 
наступного місяця. Останнім кроком ми віднімаємо один день, щоб отримати останній день поточного міся"""