grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(data: dict) -> list:
    return ["{:>4}|{:<10}|{:^5}|{:^5}".format(i, student, grade, grades[grade])
            for i, (student, grade) in enumerate(data.items(), 1)]


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)
