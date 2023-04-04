"""
Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна 
приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 
12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє 
місяць лютий високосного року.
"""

from datetime import datetime, timedelta


def get_days_in_month(month, year, day=1):
    start_date = datetime(year=year, month=month, day=day)

    end_date = (start_date + timedelta(days=32)).replace(day=day)
    days = end_date - start_date
    return int(days.total_seconds()/ (60 * 60 *24))

print(get_days_in_month(3, 2021))
