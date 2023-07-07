from datetime import datetime
import logging
from threading import Thread

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        finish = datetime.now()
        delta = finish - start
        logging.debug(f"statr: {start.time()} | finish: {finish.time()} | delta: {delta}")
        return result
        
    return wrapper

@timer
def factorize_thread(*numbers):
    results = []
    threads = []
    
    def factorize_number(number):
        factors = [i for i in range(1, number + 1) if number % i == 0]
        results.append(factors)
    
    for number in numbers:
        thread = Thread(target=factorize_number, args=(number,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]
    
    return tuple(results)


if __name__ == '__main__':
    a, b, c, d = factorize_thread(128, 255, 99999, 10651060)
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]