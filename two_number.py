"""..."""

def two_number_sum(a: str, b: str):
    """..."""
    max_num = max(len(a), len(b))
    min_num = min(len(a), len(b))
    delta = max_num - min_num
    if len(a) > len(b):
        b = ''.join(delta * '0' + b)
    else:
        a = ''.join(delta * '0' + a)
    
    result = ''
    temp_num = 0
    for i in range(max_num - 1, -1, -1):
        sum_num = int(a[i]) + int(b[i]) + temp_num
        if sum_num > 9:
            result += sum_num - 10
            temp_num = 1
        else:
            result += str(sum_num)
            temp_num = 0
        if i == 0 and temp_num == 1:
            result += temp_num
    return result[::-1]


if __name__ == "__main__":
    a =  "887"
    b = "1"
    print(two_number_sum(a, b)) #135802