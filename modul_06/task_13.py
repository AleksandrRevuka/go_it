"""Реалізуйте функцію create_archive(path, file_name, employee_residence)"""

import shutil


def create_backup(path, file_name, employee_residence):
    """create backup"""
    with open (path + '/' + file_name, 'wb') as file:
        data = list(map(lambda data: data[0] + ' ' + data[1] + '\n', employee_residence.items()))
        for line in data:
            file.write(line.encode())
    shutil.make_archive('backup_folder', 'zip', path)
    return path + '/' + 'backup_folder.zip'

if __name__ == "__main__":
    employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

    print(create_backup('modul_06', 'task_13.txt', employee_residence))
