# from collections import Counter

# def get_two_biggest(data: dict):
#     values = list(data.values())
#     keys = list(data.keys())
#     largest_values = sorted(values, reverse=True)[:2]

#     return [key for key in keys if data[key] in largest_values]

# data = {
#     'a': 34,
#     'b': 66,
#     'c': 12,
#     'd': 9000,
# }

# print(get_two_biggest(data))


# def counts_trougth(data: str):
    # way_value = 0
    # count_way = []
    # down = 'd'
    # up = 'u'
    # for move in data:
    #     if move == up:
    #         way_value += 1
    #         count_way.append(str(way_value) + up)
    #     elif move == down:
    #         way_value -= 1
    #         count_way.append(str(way_value) + down)
    # print(count_way)
    # result = Counter(count_way)
    # return result['-1d']

#     summ = count = 0
#     for s in data:
#         if s == 'd':
#             summ -= 1
#         elif s == 'u':
#             summ += 1
#         if summ == 0 and s == 'd':
#             count += 1
#     return count

# print(counts_trougth('uuuddddduudduuududduduuduudududd'))


# scores = [66, 76, 87, 45, 98, 78, 90, 45, 92, 67]

# over_75 = list(filter(lambda score: score > 75, scores))

# print(over_75)

# print(list(map(lambda x: x**2, scores)))

# fac = lambda x: x * fac(x - 1) if x else 1
# print(fac(10))


# def f_func(func):
#     """..."""
#     def f1_func(a, b):
#         print("hello")
#         if b == 0:
#             return 'No'
#         return func(a, b)
#     return f1_func


# @f_func
# def f2_func(a, b):
#     """..."""
#     return a % b

# print(f2_func(10, 5))


# def complicated(x, y):
#     return x / y


# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#     return inner


# complicated = logged_func(complicated)
# b = complicated(10, 5)


# OPERATIONS = {
#     '-': lambda x, y: x - y,
#     '+': lambda x, y: x + y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y,
# }

# tp = tuple(range(3))
# tp = list(set('3456аівфлдратсловрдлапріуепрмодлявраочвапсофіупрща'))

# print(tp)

# class Human:
#     def __init__(self, name) -> None:
#         self.name = name


#     def voice(self):
#         print(f"Hello! My name is {self.name}")

# g = Human('Tanya')
# print(g.name)
# g.name = 'Olya'
# print(g.name)

from collections import UserList

class CountableList(UserList):
    def sum(self):
        return sum(map(int, self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum()) 