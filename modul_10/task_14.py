class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            'id': self.current_id, 
            'name': name, 
            'phone': phone, 
            'email': email, 
            'favorite': favorite,
            }
        self.contacts.append(contact)
        Contacts.current_id += 1


k = Contacts()
k.add_contacts('Alex', '380633512650', 'Asmo@gmail.com', True)
k.add_contacts('Alex_1', '380633512659', 'Gvido@gmail.com', False)
print(k.list_contacts())
