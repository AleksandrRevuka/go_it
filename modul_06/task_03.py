"""Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path),
яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']"""


def read_employees_from_file(path: str) -> list:
    """read employees from file"""

    file_employees = open(path, 'r')
    employees = [employee.strip('\n') for employee in file_employees]
    file_employees.close()

    return employees


print(read_employees_from_file('modul_06//task_02.txt'))
