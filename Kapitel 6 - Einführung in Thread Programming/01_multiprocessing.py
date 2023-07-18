import multiprocessing
import os
import random
import time

def worker(num: int, sleep: int, queue: multiprocessing.Queue) -> None:
    """
    This function simulates a worker process that performs a task and puts the result in a queue.

    Args:
        num (int): The worker number.
        sleep (int): The number of seconds the worker should sleep before finishing the task.
        queue (multiprocessing.Queue): The queue to put the result in.
    """
    print(f'Worker: {num}, PID: {os.getpid()} Delay: {sleep} seconds')
    time.sleep(sleep)
    result = sleep*num
    print(f'Worker: {num} finished with result: {result}')
    queue.put(result)


if __name__ == '__main__':
    print('Program started, waiting for workers to finish')
    jobs = []
    queue = multiprocessing.Queue()
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, random.randint(1, 10), queue))
        jobs.append(p)
        p.start()
    engine = multiprocessing.Process(target=worker, args=(62, random.randint(1, 10), queue))
    engine.start()

    # Join all processes to main process
    # This will block the main process until all processes are finished
    for j in jobs:
        j.join()
    engine.join()

    out = sum(queue.get() for _ in range(queue.qsize()))
    print(f'Program finished with result: {out}')
