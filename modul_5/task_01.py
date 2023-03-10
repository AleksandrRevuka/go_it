"""Напишіть функцію real_len, яка підраховує та повертає довжину рядка
без наступних керівних символів: [\n, \f, \r, \t, \v]"""


def real_len(text):
    return len([symbol for symbol in text if symbol not in '\n, \f, \r, \t, \v'])


print(real_len('Alex\nKdfe23\t\f\v.\r'))
