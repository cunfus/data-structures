 # type: ignore | filename conflicts with stdlib

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    # O(n) - linear time
    def __str__(self):
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        
        return ', '.join(items)

    # O(1) - constant time
    def enqueue(self, value):
        if self.front is None:
            self.front = self.rear = Node(value)
        else:
            new_node = Node(value)
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    # O(1) - constant time
    def dequeue(self):
        if self.front is None:
            raise ValueError("Queue is empty")
        
        dequeue_value = self.front.value
        self.front = self.front.next
        self.size -= 1

        return dequeue_value
        
    # O(1) - constant time
    def peek(self):
        if self.front is None:
            raise ValueError("Queue is empty")
        
        return self.front.value

    def is_empty(self):
        return self.front is None

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(8)

    print(queue)
    print(queue.dequeue())
    print(queue)