from datetime import datetime
from multiprocessing import Process, Queue, cpu_count
import logging


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
        logging.debug(f"start: {start.time()} | finish: {finish.time()} | delta: {delta}")
        return result

    return wrapper


def factorize_number(number, q):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    q.put(factors)


@timer
def factorize(*numbers):
    results = []
    processes = []
    q = Queue()
    num_cores = cpu_count()


    for number in numbers:
        process = Process(target=factorize_number, args=(number, q))
        process.start()
        processes.append(process)
        
        if len(processes) >= num_cores:
            for process in processes:
                process.join()
                results.append(q.get())
            processes.clear()

    for process in processes:
        process.join()
        results.append(q.get())

    return results


if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
