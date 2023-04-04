"""
У нас є іменований кортеж для зберігання котів у змінній Cat. На першому місці у нас 
кличка котика nickname, потім його вік age та ім'я власника кота owner.
Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.
Якщо функція convert_list приймає у параметрі cats список іменованих кортежів
"""
import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats: list[Cat] | list[dict]):
    """..."""
    cats_list = []
    for cat in cats:
        if isinstance(cat, dict):
            cat = list(cat.values())
            cat_data = Cat(cat[0], cat[1], cat[2])
            cats_list.append(cat_data)
        else:
            cat_data = {"nickname": cat.nickname, "age": cat.age , "owner": cat.owner}
            cats_list.append(cat_data)
    return cats_list
            

print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))

print(convert_list([
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]))