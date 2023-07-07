"""
Потік у функції
У процесі створення екземпляра класу Thread можна передати аргументу target функцію 
та передати їй аргументи:
"""

from threading import Thread
from datetime import datetime
import logging

def fibo(n):
    if n > 2:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return 1
    
def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        delta = finish - start
        print (f"statr: {start.time()} | finish: {finish.time()} | delta: {delta}")
        
    return wrapper

@timer
def example_work(k):
    logging.debug('Wake up!')
    num_fibo = fibo(k)    
    logging.debug(f"fibo({k}): {num_fibo}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(35, 40):
        thread = Thread(target=example_work, args=(i,))
        thread.start()