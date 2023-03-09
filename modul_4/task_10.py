from random import randint


def get_random_password():
    return ''.join([chr(randint(40, 126)) for _ in range(8)])
