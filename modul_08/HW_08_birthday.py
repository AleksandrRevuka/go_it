
from datetime import datetime, timedelta
from prettytable import PrettyTable


USERS = [
    {"name": "Андрій", "birthday": datetime(1990, 4, 1)},
    {"name": "Олександр", "birthday": datetime(1991, 4,2)},
    {"name": "Ірина", "birthday": datetime(1992, 4, 3)},
    {"name": "Марія", "birthday": datetime(1989, 4, 4)},
    {"name": "Володимир", "birthday": datetime(1987, 4, 5)},
    {"name": "Наталя", "birthday": datetime(1994, 4, 6)},
    {"name": "Юлія", "birthday": datetime(1993, 4, 7)},
    {"name": "Олег", "birthday": datetime(1990, 4, 8)},
    {"name": "Євгенія", "birthday": datetime(1991, 4, 9)},
    {"name": "Віктор", "birthday": datetime(1988, 4, 10)},
    {"name": "Катерина", "birthday": datetime(1995, 4, 11)},
    {"name": "Оксана", "birthday": datetime(1992, 4, 12)},
    {"name": "Дмитро", "birthday": datetime(1986, 4, 13)},
    {"name": "Тетяна", "birthday": datetime(1996, 4, 14)},
    {"name": "Аліна", "birthday": datetime(1994, 4, 15)},
    {"name": "Максим", "birthday": datetime(1985, 4, 16)},
    {"name": "Сергій", "birthday": datetime(1993, 4, 17)},
    {"name": "Надія", "birthday": datetime(1990, 4, 18)},
    {"name": "Анна", "birthday": datetime(1997, 4, 19)},
    {"name": "Павло", "birthday": datetime(1989, 4, 20)}
]


def get_birthdays_per_week(users):
    """
    Prints a table of the birthdays for each day of the week. 
    Users whose birthdays fall on a weekend are listed on the following Monday.
    """
    weekend_days = ["Saturday", "Sunday"]
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    users_birthday = {day: [] for day in days_of_week}

    date_week = []
    current_date = datetime.now().date()
    current_year = str(current_date.year)

    for day in range(0, 7):
        date = current_date + timedelta(days=day)
        date = date.strftime('%d %B')
        date_week.append(date)

    for user in users:
        user_date = user['birthday'].strftime('%d %B')
        if user_date in date_week:
            user_date = user_date + ' ' + current_year
            user_date_now = datetime.strptime(user_date, '%d %B %Y').date()

            day_of_week = user_date_now.strftime('%A')
            name = user['name']

            if day_of_week in weekend_days:
                users_birthday['Monday'].append(name)
            else:
                users_birthday[day_of_week].append(name)

    table = PrettyTable()
    table.field_names = ["Day of Week", "Birthdays 🎉 🎂 🎁"]

    for day, birthdays in users_birthday.items():
        table.add_row([day, f"{', '.join(birthdays)}" if birthdays else "-"])

    print(table)


if __name__ == '__main__':
    get_birthdays_per_week(USERS)
