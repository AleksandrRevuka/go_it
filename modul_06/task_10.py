"""Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає
інформацію про користувачів з паролями в бінарний файл."""


def save_credentials_users(path, users_info):
    data = [(key + ':' + value + '\n').encode() for key, value in users_info.items()]
    with open(path, 'wb') as file_bin:
        file_bin.writelines(data)




users_info = {
    'andry':'uyro18890D',
    'steve':'oppjM13LL9e'
    }

save_credentials_users('modul_06//task_10.bin', users_info)
