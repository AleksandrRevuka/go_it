"""Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного
співробітника починалася з нового рядка."""


def write_employees_to_file(employee_list: list, path: str):
    """write employees to file"""
    file_emploee = open(path, 'w')

    for department in employee_list:
        for employee in department:
            file_emploee.write(employee + '\n')
    file_emploee.close()


write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],
                        'modul_06//task_02.txt')
