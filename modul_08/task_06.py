"""
Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє 
арифметичне типу Decimal з кількістю значущих цифр signs_count. 
Параметр number_list — список чисел
"""
from decimal import Decimal, getcontext
    

def decimal_average(number_list, signs_count):
    """..."""
    getcontext().prec = signs_count
    return sum(list(map(Decimal, number_list))) / len(number_list)
    
        
print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))
