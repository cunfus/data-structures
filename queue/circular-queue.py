
class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
    
    def __repr__(self):
        return f"{self.queue}, front:{self.front}, rear:{self.rear}"
    
    # O(n) - linear time
    def __str__(self):
        items = []
        index = self.front
        for _ in range(self.capacity):
            if index != self.rear:
                items.append(str(self.queue[index]))
                index = (index + 1) % self.capacity
        
        return ', '.join(items)

    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    # O(1) - constant time
    def enqueue(self, value):
        if self.is_full():
            raise IndexError("queue is full.")
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
    
    # O(1) constant time
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty.")
        else:
            ret_value = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return ret_value
    
    def get_size(self):
        return (self.rear + self.capacity - self.front) % self.capacity
    

if __name__ == "__main__":
    
    cycle_queue = CircularQueue(8)

    for i in range(7):
        cycle_queue.enqueue(i)
    print(cycle_queue)

    for i in range(5):
        cycle_queue.dequeue()
    print(cycle_queue)    

    for i in range(9, 14):
        cycle_queue.enqueue(i)
    print(cycle_queue)

