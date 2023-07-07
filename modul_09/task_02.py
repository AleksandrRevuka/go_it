"""
Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину 
з урахуванням знижки клієнта.

Функція приймає два параметри:

price — ціна продукту
customer — словник з даними клієнта такого виду: {"name": "Dima"} або {"name": "Boris", "discount": 0.15}
Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, якщо у нього немає поля discount.

Функція get_discount_price_customer має повертати нову ціну товару для клієнта.

Нагадаємо, що дисконт discount - це дробове число від 0 до 1. І ми під знижкою розуміємо коефіцієнт, 
який визначає величину ціни. І на цю величину ми знижуємо підсумкову ціну товару: price = price * (1 - discount).
"""

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    """..."""
    if len(customer) > 1:
        return price * (1 - customer['discount'])

    return price * (1 - DEFAULT_DISCOUNT)


print(get_discount_price_customer(120, {"name": "Boris", "discount": 0.15}))
print(get_discount_price_customer(120, {"name": "Boss",}))