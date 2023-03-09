def prepare_data(data: list):
    data.sort()
    data.pop(0)
    data.reverse()
    data.pop(0)
    return sorted(data)