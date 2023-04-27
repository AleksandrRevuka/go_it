import json


def write_contacts_to_file(filename, contacts):
    """..."""
    with open(filename, 'w', encoding='utf8') as file:
        data = {}
        data['contacts'] = contacts
        json.dump(data, file) 
        

def read_contacts_from_file(filename):
    """..."""
    with open(filename, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data['contacts']
        
    
