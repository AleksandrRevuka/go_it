def normal_name(list_name):
    return list(map(lambda name: name.capitalize(), list_name))

print(normal_name(["dan", "jane", "steve", "mike"]))