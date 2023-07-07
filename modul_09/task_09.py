"""
На початку четвертого модуля ми вирішували завдання виплат за комунальними платежами. 
Вони являли собою список payment з додатними та від'ємними значеннями. Створіть функцію 
positive_values та за допомогою функції filter відфільтруйте список payment за додатними 
значеннями, та поверніть його з функції.
"""

def positive_values(list_payment):
    return list(filter(lambda number: number > 0, list_payment))


payment = [100, -3, 400, 35, -100]
print(positive_values(payment))
