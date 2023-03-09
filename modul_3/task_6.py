def format_string(string, length):
    if len(string) >= length:
        return string
    if len(string) < length:
        return f"{(length - len(string)) // 2 * ' '}{string}"


format_string(string='abaa', length=15)
