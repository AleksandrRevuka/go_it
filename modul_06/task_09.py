"""Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка
повертає True, якщо рядки дорівнюють собі, і False — якщо ні."""


def is_equal_string(utf8_string, utf16_string):
    """is equal string"""
    utf8_string = utf8_string.decode()
    utf16_string = utf16_string.decode('utf-16')
    utf8_string, utf16_string = utf8_string.casefold(), utf16_string.casefold()
    if utf8_string == utf16_string:
        return True
    else:
        return False
