
from datetime import datetime
from prettytable import PrettyTable


USERS = [
    {"name": "Андрій", "birthday": datetime(1990, 3, 15)},
    {"name": "Олександр", "birthday": datetime(1991, 3,20)},
    {"name": "Ірина", "birthday": datetime(1992, 3, 20)},
    {"name": "Марія", "birthday": datetime(1989, 3, 15)},
    {"name": "Володимир", "birthday": datetime(1987, 3, 16)},
    {"name": "Наталя", "birthday": datetime(1994, 3, 20)},
    {"name": "Юлія", "birthday": datetime(1993, 3, 18)},
    {"name": "Олег", "birthday": datetime(1990, 3, 17)},
    {"name": "Євгенія", "birthday": datetime(1991, 3, 21)},
    {"name": "Віктор", "birthday": datetime(1988, 3, 15)},
    {"name": "Катерина", "birthday": datetime(1995, 3, 17)},
    {"name": "Оксана", "birthday": datetime(1992, 3, 15)},
    {"name": "Дмитро", "birthday": datetime(1986, 3, 21)},
    {"name": "Тетяна", "birthday": datetime(1996, 3, 18)},
    {"name": "Аліна", "birthday": datetime(1994, 3, 14)},
    {"name": "Максим", "birthday": datetime(1985, 3, 19)},
    {"name": "Сергій", "birthday": datetime(1993, 3, 17)},
    {"name": "Надія", "birthday": datetime(1990, 3, 20)},
    {"name": "Анна", "birthday": datetime(1997, 3, 18)},
    {"name": "Павло", "birthday": datetime(1989, 3, 20)}
]


def get_birthdays_per_week(users):
    """
    Prints a table of the birthdays for each day of the week. 
    Users whose birthdays fall on a weekend are listed on the following Monday.
    """
    weekend_days = ["Saturday", "Sunday"]
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    users_birthday = {day: [] for day in days_of_week}

    for user in users:
        day_of_week = user['birthday'].strftime('%A')
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
