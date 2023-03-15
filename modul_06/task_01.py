"""Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл
 і повертати загальну суму заробітної плати всіх розробників компанії."""


def total_salary(path: str) -> float:
    """total salary"""

    file = open(path, 'r')
    salary = sum([float(line.split(",")[1]) for line in file])
    file.close()
    return salary


print(total_salary('modul_06//task_01.txt'))
