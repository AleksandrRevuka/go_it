"""Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path -
 шлях до файлу) буде додавати співробітника (параметр record) у вигляді рядка "Drake
 Mikelsson,19"."""


def add_employee_to_file(record: str, path: str):
    """add employee to file"""

    file_emploees = open(path, 'a')
    file_emploees.write(record + '\n')
    file_emploees.close()


add_employee_to_file('Alex Rotanovich,24', 'modul_06//task_02.txt')
