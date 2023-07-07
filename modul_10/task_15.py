"""
Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод 
get_contact_by_id. Метод повинен шукати контакт по унікальному id у списку contacts та повертати 
словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не 
знайдено, метод повертає None.
"""

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if id == contact['id']:
                return contact
        return None
    

k = Contacts()
k.add_contacts('Alex', '380633512650', 'Asmo@gmail.com', True)
k.add_contacts('Alex_1', '380633512659', 'Gvido@gmail.com', False)
print(k.list_contacts())
print(k.get_contact_by_id(2))