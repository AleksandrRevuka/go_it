"""Розробіть функцію save_applicant_data(source, output), яка буде
вказаний список із параметра source зберігати у файл із параметра output"""


# def save_applicant_data(source: list, output: str):
#     """save applicant data"""
#     student = [','.join(str(data) for data in data_student.values()) + '\n' for data_student in source]
#     with open(output, 'w') as file_data:
#             file_data.writelines(student)


# def save_applicant_data(source: list, output: str):
#     list1 = [','.join(map(str, i.values())) + '\n' for i in source]
#     print(list1)

#     with open(output, 'w') as file_data:
#         file_data.writelines(list1)


def save_applicant_data(source: list, output: str):
    """save applicant data"""
    with open(output, 'w') as file_data:
        for data_student in source:
            new_format_data_student = ','.join(str(data) for data in data_student.values()) + '\n'
            file_data.write(new_format_data_student)


sourc = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
    ]

save_applicant_data(sourc, 'modul_06//task_08.txt')
