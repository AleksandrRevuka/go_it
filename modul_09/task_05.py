def format_phone_number(func):
    def add_code_phone(phone):
        phone = func(phone)

        if len(phone) == 12:
            return ''.join('+' + phone)

        return ''.join('+38' + phone)

    return add_code_phone


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number('380501233234'))
print(sanitize_phone_number('0501233234'))