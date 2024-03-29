"""
Завершуємо функціональність класу Contacts. На цьому етапі ми додамо до класу метод remove_contacts. 
Метод винен видаляти контакт по унікальному id у списку contacts. Якщо словника із зазначеним id у 
списку contacts не знайдено, метод жодних дій над списком contacts не робить.
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
    
    def remove_contacts(self, id):
        for contact in self.contacts:
            if id == contact['id']:
                self.contacts.remove(contact)