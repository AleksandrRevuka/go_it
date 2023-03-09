def get_fullname(first_name=None, last_name=None, middle_name=None):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"


get_fullname(first_name=None, last_name=None, middle_name=None)