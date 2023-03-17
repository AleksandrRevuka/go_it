numbers = ['1', '2', '3', '4']
words = ["Welcome", "to", "Real", "Python"]

dict_words = dict(zip(numbers, words))
print(dict_words)

list_words = list(map(lambda n: n[0] + ':' + n[1], dict_words.items()))
print(list_words)


list_words = list(map(lambda n, k: n + ':' + k, numbers, words))
print(list_words)
