"""hhd"""


def formatted_numbers() -> list:
    """formatted_numbers"""
    header = "|{:^9} |{:^9} |{:^10}|".format('decimal', 'hex', 'binary')
    result = ["|{0:<9d} |{0:^9x} |{0:>10b}|".format(number) for number in range(1, 15)]
    result.insert(0, header)
    return result


for el in formatted_numbers():
    print(el)
