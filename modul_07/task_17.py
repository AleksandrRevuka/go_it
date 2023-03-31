def encode(data):
    if not data:
        return []

    encode_list = []
    symbol, *_ = data
    count = 1
    for i, symb in enumerate(data):
        if i >= 1:
            if data[i - 1] == symb:
                count +=1
            else:
                break

    encode_list.append(symbol)
    encode_list.append(count)
    
    data = data[count:]
    encode_list.extend(encode(data))
    return encode_list
    
    
print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))