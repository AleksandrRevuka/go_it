def sanitize_phone_number(phone):
    return ''.join([number.strip(' , (, ), -, +') for number in phone])


print(sanitize_phone_number("   38050-111- 22-22   "))
