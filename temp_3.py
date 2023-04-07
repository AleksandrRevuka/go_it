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


scores = [66, 76, 87, 45, 98, 78, 90, 45, 92, 67]

over_75 = list(filter(lambda score: score > 75, scores))

print(over_75)

print(list(map(lambda x: x**2, scores)))

fac = lambda x: x * fac(x - 1) if x else 1
print(fac(10))