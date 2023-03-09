def amount_payment(payments):
    return sum([payment if payment >= 0 else 0 for payment in payments])