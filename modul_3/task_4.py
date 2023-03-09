def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        discount = price * discount
        return price - discount

    price = apply_discount()
    return price


if __name__ == '__main__':
    discount_price(price=0, discount=0)