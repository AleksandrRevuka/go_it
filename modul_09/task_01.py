"""
Минулого разу ми реалізували дві функції. Перша - get_grade, приймає ключ в оцінці ECTS і 
повертає відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга - get_description, теж 
приймає ключ у оцінки ECTS, але повертає пояснення оцінки у текстовому форматі (останній стовпчик 
таблиці). На неіснуючий ключ функції повинні повертати значення None.

Реалізуйте функцію вищого порядку get_student_grade, яка приймає параметр option. Якщо він 
дорівнює значенням "grade", то функція повертає функцію get_grade, а якщо його значення дорівнює 
"description", то повертає функцію get_description. Якщо параметр за значенням не співпав із 
заданими, то функція get_student_grade повинна повертати значення None.
"""
def get_grade(key):
    """..."""
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    """..."""
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option: str):
    """..."""
    if option == 'grade':
        return get_grade

    if option == 'description':
        return get_description

    return None

