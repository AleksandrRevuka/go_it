def decode(data):
    if not data:
        return []

    decode_list = []
    symbol, count, *tail = data
    
    while count > 0:
        decode_list.append(symbol)
        count -= 1
        
    decode_list.extend(decode(tail))
    return decode_list
    
    
    
print(decode(['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]))