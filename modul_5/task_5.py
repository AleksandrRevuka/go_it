def sanitize_phone_number(phone):
    return ''.join([number.strip(' , (, ), -, +') for number in phone])


def get_phone_numbers_for_countries(list_phones):
    cleaned_phones = [sanitize_phone_number(phone) for phone in list_phones]
    sorted_phones = {
        "UA": [phone for phone in cleaned_phones if phone.startswith('380') or phone.startswith('0')],
        "JP": [phone for phone in cleaned_phones if phone.startswith('81')],
        "TW": [phone for phone in cleaned_phones if phone.startswith('886')],
        "SG": [phone for phone in cleaned_phones if phone.startswith('65')]
        }
    return sorted_phones


print(get_phone_numbers_for_countries(['+3806 3456-7658', '+81 345 56 78--', ' 88(656)7-82-34',
                                       '65 567 45 34 ', '6 5 555 45 67', '25 456 78 23 ', '063 352 23 43']))
