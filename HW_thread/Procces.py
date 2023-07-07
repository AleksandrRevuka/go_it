from multiprocessing import Process
import logging
from datetime import datetime
from random import randint

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self) -> None:
        params, k = self.args
        example_work(params, k)
        logger.debug(params)
        

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
def example_work(params, k):
    num_fibo = fibo(k)    
    logging.debug(f"fibo({k}): {num_fibo}")
    logger.debug(params)


if __name__ == '__main__':
    processes = []
    # for i in range(10):
    #     k = randint(37,37)
    #     pr = Process(target=example_work, args=(f"Count process function - {i}", k))
    #     pr.start()
    #     processes.append(pr)

    for i in range(10):
        k = randint(37,37)
        pr = MyProcess(args=(f"Count process class - {i}", k,))
        pr.start()
        processes.append(pr)

    [el.join() for el in processes]
    logger.debug('End program')
