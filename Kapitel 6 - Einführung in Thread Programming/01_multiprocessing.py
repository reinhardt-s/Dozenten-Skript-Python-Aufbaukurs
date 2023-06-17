import multiprocessing
import os
import random
import time


def worker(num, sleep, queue):
    print(f'Worker: {num}, PID: {os.getpid()} Delay: {sleep} seconds')
    time.sleep(sleep)
    result = sleep*num
    print(f'Worker: {num} finished with result: {result}')
    # Since we are in a different process, we need to use a queue to communicate with the main process
    queue.put(result)


if __name__ == '__main__':
    print('Programm started, waiting for workers to finish')
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

    out = 0
    # Get results from queue
    while not queue.empty():
        result = queue.get()
        print(f'Got result from queue: {result}')
        out += result

    print(f'Programm finished with result: {out}')


