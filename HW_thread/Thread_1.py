"""
Потік як функтор
Є інший спосіб виконати код окремого потоку. Для цього потрібно, щоб код виконання був
функтором (функцією або класом, який має метод __call__). Тоді об'єкт можна передати 
як іменований аргумент target у Thread:
"""

from threading import Thread
from time import sleep
import logging
from datetime import datetime


def fibo(n):
    if n > 2:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return 1
    
def timer(func):
    def wrapper(args):
        start = datetime.now()
        func(args)
        finish = datetime.now()
        delta = finish - start
        print (f"statr: {start.time()} | finish: {finish.time()} | delta: {delta}")
        
    return wrapper


class UsefulClass():
    def __init__(self, second_num):
        self.delay = second_num

    @timer
    def __call__(self):
        
        logging.debug('Wake up!')

        num_fibo = fibo(self.delay)
        
        logging.debug(f"fibo({self.delay}): {num_fibo}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(39)
    thread = Thread(target=t2)
    thread.start()
    print('Some stuff')