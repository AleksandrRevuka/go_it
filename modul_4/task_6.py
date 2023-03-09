def split_list(grade):
    if grade:
        average_grade = sum(grade) / len(grade)
        min_num = [number for number in grade if number <= average_grade]
        max_num = [number for number in grade if number > average_grade]
    else:
        return [], []
    return min_num, max_num
