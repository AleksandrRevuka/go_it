def make_request(keys, values):
    if len(keys) == len(values):
        return dict(zip(keys, values))
    return {}
    
print(make_request(['При', 'роботі', 'веб'], ['необхідність', 'використовувати', 'словник']))    