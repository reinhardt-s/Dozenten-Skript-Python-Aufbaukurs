import threading
import time
import queue


def worker(q):
    print('Starting worker')
    time.sleep(5)
    print('Finished worker')
    q.put('Hello from worker!')


if __name__ == '__main__':
    q = queue.Queue()
    t = threading.Thread(target=worker, args=(q,))
    t.start()

    # Join waits for the thread to finish, or timeout after 10 seconds
    t.join(timeout=10)

    if t.is_alive():
        print('The worker is still running')
    else:
        print('The worker has finished')
        if not q.empty():
            result = q.get()
            print('Worker returned:', result)
