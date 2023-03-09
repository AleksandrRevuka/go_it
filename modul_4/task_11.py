from string import ascii_lowercase, ascii_uppercase, digits


def is_valid_password(password):
    valid_number = False
    valid_lowercase = False
    valid_uppercase = False

    if len(password) < 8 or len(password) > 8:
        return False

    for symbol in password:
        if symbol in ascii_lowercase:
            valid_lowercase = True
        elif symbol in ascii_uppercase:
            valid_uppercase = True
        elif symbol in digits:
            valid_number = True
    return valid_number and valid_uppercase and valid_lowercase
