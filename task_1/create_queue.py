from queue import Queue
from numpy import random
import time
queue = Queue()


def generate_request():
    task = {f'unique number: {random.randint(100)}'}
    queue.put(task)
    print(task)
    time.sleep(1)

def process_request():
    if queue.qsize() > 0:
        current = queue.get()
        print(f"In work: {current}")
        time.sleep(1.1)
    else:
        print('The queue is empty')

while True:
    generate_request()

    process_request()
