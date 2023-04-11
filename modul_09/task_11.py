"""
Для списку numbers підрахувати суму елементів за допомогою функції reduce.

Створіть функцію sum_numbers(numbers), результатом виконання якої буде сума 
чисел всіх елементів списку numbers.
"""
from functools import reduce


def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

number = [3, 4, 6, 9, 34, 12]

print(sum_numbers(number))