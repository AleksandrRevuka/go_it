from random import randint
import random
import string


def binary_serch(data: list, item: str):
    low = 0
    high = len(data) - 1
    
    count = 0
    while low <= high:
        count += 1
        mid = (low + high)
        guess = data[mid]
        if guess == item:
            return mid, count
        
        if guess > item:
            high = mid - 1
        
        else:
            low = mid + 1
            
    return None



def binary_serch_2(data: list, item: int):
    low = 0
    high = len(data) - 1
    
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = data[mid]
        if guess == item:
            return mid, count
        
        if guess < item:
            low = mid
        
        else:
            high = mid
            
    return None


def binary_serch_3(data: list, item: int):
    low = 0
    high = len(data) - 1
    item_index = data.index(item)
    
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = data[mid]

        if guess == item:
            return guess, count
        
        if mid < item_index:
            low = mid
        
        else:
            high = mid
            
    return None


def gen_names(counter):
    
    names = []
    for _ in range(counter):
        name_length = random.randint(3, 15)
        name = ''.join(random.choice(string.ascii_letters) for _ in range(name_length))
        names.append(name)
        
    return names


max_item = 1_000_000_00

# data_list = list(range(0, max_item))

names_data = gen_names(max_item)
serch_item = names_data[randint(0, max_item)]
print(serch_item)

# print(binary_serch(data_list, serch_item))
print(binary_serch_3(names_data, serch_item))
