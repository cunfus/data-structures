
class RingBuffer:

    def __init__(self, capacity, overwrite=True):
        self.capacity = capacity
        self.buffer = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.overwrite = overwrite
    
    def __repr__(self):
        return f"{self.buffer}, front:{self.front}, rear:{self.rear}"
    
    # O(n) - linear time
    def __str__(self):
        items = [self.buffer[(self.front + i) % self.capacity] for i in range(self.size)]
        return ', '.join(map(str, items))

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    # O(1) - constant time
    def enqueue(self, value):
        if self.is_full():
            if self.overwrite == False:
                raise IndexError("buffer is full.")
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

        self.buffer[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    # O(1) constant time
    def dequeue(self):
        if self.is_empty():
            raise IndexError("buffer is empty.")
        else:
            ret_value = self.buffer[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

            return ret_value
    
    def get_size(self):
        return self.size
    

if __name__ == "__main__":
    
    buf = RingBuffer(4)

    buf.enqueue(1)
    buf.enqueue(2)
    buf.enqueue(3)
    buf.enqueue(4)
    print(buf)

    buf.enqueue(5)
    print(buf)

    print(buf.dequeue())
    print(buf)
    
