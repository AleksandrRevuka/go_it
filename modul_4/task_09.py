def is_valid_pin_codes(pin_codes):
    validate = False
    if len(set(pin_codes)) != len(pin_codes):
        return False
    for pin_code in pin_codes:
        if pin_code and pin_code.isdigit() and len(pin_code) == 4:
            validate = True
        else:
            return False
    return validate
