"""
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, який 
містить електронні адреси всіх контактів зі списку list_contacts. Використовуйте функцію map.
"""

def get_emails(list_contacts):
    """..."""
    # return [contact["email"] for contact in list_contacts]
    return list(map(lambda email: email["email"], list_contacts))



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

print(get_emails(contacts))