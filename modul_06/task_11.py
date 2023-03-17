"""Реалізуйте функцію get_credentials_users(path), яка повертає список рядків
із бінарного файлу, створеного в попередньому завданню"""


def get_credentials_users(path: list):
    """get credentials users"""
    with open(path, 'rb') as file_bin:
        result = [line.decode() for line in file_bin]
        return [el.strip('\n') for el in result]


if __name__ == "__main__":
    print(get_credentials_users('modul_06//task_10.bin'))
