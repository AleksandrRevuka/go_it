"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з 
числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, 
необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
"""
from random import randrange, sample


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        data = list(range(min, max))
        result = sample(data, k=quantity)
        return sorted(result)
    return []

print(get_numbers_ticket(2, 7, 5))