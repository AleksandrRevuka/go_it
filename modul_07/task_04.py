def is_integer(s: str):
    s = s.strip()
    s = s.strip('+-')
    if len(s) == 0:
        return False
    if s.isdigit():
        return True
    return False


print(is_integer('-a45'))