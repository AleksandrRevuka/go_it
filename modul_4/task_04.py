def get_grade(key):
    grade_number = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
    if key not in grade_number.keys():
        return None
    return grade_number[key]


def get_description(key):
    grade_number = {'F': "Unsatisfactorily", 'FX': "Unsatisfactorily", 'E': "Enough", 'D': "Satisfactorily",
                    'C': "Good", 'B': "Very good", 'A': "Perfectly"}
    if key not in grade_number:
        return None
    return grade_number[key]
