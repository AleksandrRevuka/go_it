import csv


def write_contacts_to_file(filename, contacts):
    """..."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        field_names = ['name', 'email', 'phone', 'favorite']
        data = csv.DictWriter(file, fieldnames=field_names)
        for contact in contacts:
            data.writeheader()
            data.writerow({
                'name': contact['name'], 
                'email': contact['email'], 
                'phone': contact['phone'], 
                'favorite': contact['favorite'],
                })


def read_contacts_from_file(filename):
    """..."""
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        return [{**contact, 'favorite': contact['favorite']=='True'} for contact in list(csv.DictReader(file))]
    #     data = []
    #     for contact in list(csv.DictReader(file)):
    #         if contact['favorite'] == 'False':
    #             contact['favorite'] = False
    #             data.append(contact)
    #         else:
    #             contact['favorite'] = True
    #             data.append(contact)
    # return data



data_x = [{
    'name': 'Allen Raymond', 
    'email': 'nulla.ante@vestibul.co.uk', 
    'phone': '(992) 914-3792', 
    'favorite': 'False',
    }, {
    'name': 'Chaim Lewis', 
    'email': 'dui.in@egetlacus.ca', 
    'phone': '(294) 840-6685', 
    'favorite': 'True',
    }]

# data_y = []
# for contact in data_x:
#     contact['favorite'] = bool(contact['favorite'])
#     data_y.append(contact)

data_y = [contact if contact['favorite'] == 'True' else {**contact, 'favorite': False} for contact in data_x]
data_y = list(map(lambda contact: {**contact, 'favorite': True} if contact['favorite'] == 'True' else {**contact, 'favorite': False}, data_x))
print(data_y)

data_u = list(map(lambda contact: {**contact, 'favorite': contact['favorite']=='True'}, data_x))
print(data_u)


data_y = [{**contact, 'favorite': contact['favorite']=='True'} for contact in data_x]
print(data_y)