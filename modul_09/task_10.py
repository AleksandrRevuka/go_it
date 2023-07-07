"""
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. 
Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.
"""
def get_favorites(contacts):
    """..."""
    return list(filter(lambda contact: contact["favorite"], contacts))

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}, {
    "name": "Allen Python",
    "email": "google.ante@co.uk",
    "phone": "(099) 914-3892",
    "favorite": True,
}]


print(get_favorites(contacts))
