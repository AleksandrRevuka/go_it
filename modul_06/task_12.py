"""Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data
зазначений список, виконує кодування кожної пари username:password у формат Base64
та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']"""


from base64 import b64encode

from task_11 import get_credentials_users


def encode_data_to_base64(data):
    """encode data to base64"""
    return [b64encode(user.encode()).decode() for user in data]

if __name__ == "__main__":
    data_for_encode = get_credentials_users('modul_06//task_10.bin')
    print(data_for_encode)
    print(encode_data_to_base64(data_for_encode))
