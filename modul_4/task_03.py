def format_ingredients(items):
    for i, item in enumerate(items):
        check = any(symbol.isdigit() for symbol in item)
        if not check:
            result = "".join(items[i - 1] + ' and ' + items[i])
            del items[i - 1]
            del items[i - 1]
            items.append(result)
    return ", ".join(items)
