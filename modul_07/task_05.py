def capital_text(text):
    
    new_text = ""
    for i, _ in enumerate(text):
        if i == 0:
            new_text += text[i].upper()
        elif text[i-2] in ['.', '!', '?']:
            new_text += text[i].upper()
        else:
            new_text += text[i]
    return new_text
    
    
print(capital_text("hi my name Sasha! i want to drink coffee. what should I do? i don't understand."))