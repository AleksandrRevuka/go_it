"""sorted"""


def sorted_numder(function, object):
    result = sorted(function(object), reverse=True)
    return ' '.join(result)


def str_numder_list(numbers_str):
    return list(map(str, numbers_str))


def str_number_dict(numbers_dict):
    return list(map(str, numbers_dict.values()))


numbers = [1, 2, 3, 4]
dict_num = {'a': 10, 'b': 20, 'c': 30, 'd': 40,}

print(sorted_numder(str_numder_list, numbers))
print(sorted_numder(str_number_dict, dict_num))
