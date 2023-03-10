def is_check_name(fullname, first_name):
    return ''.join(fullname.split(' ')).startswith(first_name)


print(is_check_name('Revuka Oleksandr', 'Revuka'))
