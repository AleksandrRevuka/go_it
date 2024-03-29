import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_person = Person(self.name, self.email, self.phone, self.favorite)
        copy_person.name = copy.copy(self.name)
        copy_person.email = copy.copy(self.email)
        copy_person.phone = copy.copy(self.phone)
        copy_person.favorite = copy.copy(self.favorite)
        return copy_person    
            

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_contacts = Contacts(self.filename, self.contacts)
        copy_contacts.filename = copy.copy(self.filename)
        copy_contacts.contacts = copy.copy(self.contacts)
        copy_contacts.is_unpacking = copy.copy(self.is_unpacking)
        copy_contacts.count_save = copy.copy(self.count_save)
        return copy_contacts

    def __deepcopy__(self, memo):
        d_copy_contacts = Contacts(self.filename, self.contacts)
        memo[id(d_copy_contacts)] = d_copy_contacts
        d_copy_contacts.filename = copy.deepcopy(self.filename)
        d_copy_contacts.contacts = copy.deepcopy(self.contacts)
        d_copy_contacts.is_unpacking = copy.deepcopy(self.is_unpacking)
        d_copy_contacts.count_save = copy.deepcopy(self.count_save)
        return d_copy_contacts
    