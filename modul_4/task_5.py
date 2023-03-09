def lookup_key(data, value):
    return [key for key, value_current in data.items() if value == value_current]
