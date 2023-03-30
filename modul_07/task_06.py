def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
        start_index = riddle.find(start_letter)
        if start_index == -1:
            return ""
        end_index = start_index + word_length
        return riddle[start_index:end_index]
    
    start_index = riddle.find(start_letter)
    if start_index == -1:
        return ""
    end_index = start_index + word_length
    return riddle[start_index:end_index]


print(solve_riddle('mi1rewopret', 5, 'p', True))
print(solve_riddle('mi1powerret', 5, 'p'))