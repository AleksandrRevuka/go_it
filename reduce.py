from functools import reduce

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers = [1, 3, 7, 10, 14]

print(reduce(my_add, numbers))

min_value, k, *rest = numbers
print(f'{min_value}  ..... {rest}')
