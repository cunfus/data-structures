import sys
import os
sys.path.append(os.path.dirname(__file__))

from queue import Queue

import threading

class BlockingQueue:

    def __init__(self, max_size):
        self.queue = Queue()
        self.max_size = max_size
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)
    
    def put(self, item):
        with self.not_full:
            while len(self.queue) >= self.max_size:
                self.not_full.wait()

            self.queue.enqueue(item)

            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait()

            item = self.queue.dequeue()

            self.not_full.notify()
            return item


# ----------------------------- testing -------------------------------

import time

def producer(block_queue, stop_event):
    sequence = 1
    while stop_event.is_set():
        time.sleep(1.5)
        block_queue.put(sequence)
        print(f"producer: {sequence}")
        sequence += 1

def consumer(block_queue, stop_event):
    while stop_event.is_set():
        time.sleep(1)
        print(f"consumer: {block_queue.get()}")

if __name__ == "__main__":

    block_queue = BlockingQueue(5)

    stop_event = threading.Event()
    stop_event.set()

    producer_thread = threading.Thread(target=producer, args=(block_queue, stop_event))
    consumer_thread = threading.Thread(target=consumer, args=(block_queue, stop_event))

    producer_thread.start()
    consumer_thread.start()

    time.sleep(10)
    stop_event.clear()

    producer_thread.join()
    consumer_thread.join()
