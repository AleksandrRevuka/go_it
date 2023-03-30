def flatten(data):
    if not data:
        return []
    flattened = []
    for element in data:
        if isinstance(element, list):
            flattened.extend(flatten(element))
        else:
            flattened.append(element)
    return flattened

print(flatten([1, 2, [3, 4, [5, 6]], 7]))