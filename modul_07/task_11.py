def filter_text_message(text_message: str,  keys_table: dict):
    filtered_message = ''
    for symbol in text_message:
        symbol = symbol.lower()
        if symbol in keys_table:
            filtered_message += symbol
    return filtered_message


def encode_message(filtered_message: str, keys_table: dict):
    encoded_message = ''
    for symbol in filtered_message:
        if symbol in keys_table:
            encoded_message += str(keys_table[symbol])
    return encoded_message


def sequence_buttons(string):
    phone_keys_table = {
        '.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111,
        'a': 2, 'b': 22, 'c': 222,
        'd': 3, 'e': 33, 'f': 333,
        'g': 4, 'h': 44, 'i': 444,
        'j': 5, 'k': 55, 'l': 555,
        'm': 6, 'n': 66, 'o': 666,
        'p': 7, 'q': 77, 'r': 777, 's': 7777,
        't': 8, 'u': 88, 'v': 888,
        'w': 9, 'x': 99, 'y': 999, 'z': 9999,
        ' ': 0
    }
    filtered_message = filter_text_message(string, phone_keys_table)
    return encode_message(filtered_message, phone_keys_table)