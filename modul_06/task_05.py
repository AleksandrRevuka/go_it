"""Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]"""


def get_cats_info(path: str) -> dict:
    """get cats info"""
    parameters = ['id', 'name', 'age']
    cats = []

    with open(path, 'r') as cats_info:
        for line in cats_info:
            data_clean = line.strip('\n')
            data = data_clean.split(',')
            cats.append(dict(zip(parameters, data)))
    return cats


print(get_cats_info('modul_06//task_05.txt'))
