from threading import Thread, Timer
from datetime import datetime
import logging
from random import randint
from time import sleep



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
    logging.debug('Start program')
    
    print(datetime.now().time())
    first = Timer(0, example_work, args=(40, ))
    first.name = 'First thread'
    print(datetime.now().time())
    second = Timer(10, example_work, args=(42, ))
    second.name = 'Second thread'
    logging.debug('Start timers')
    first.start()
    second.start()
    
    # second.cancel()
    
    first.join()
    second.join()

    logging.debug('End program')
