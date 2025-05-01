
class Node:
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque():

    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0
    
    def __len__(self):
        return self.size

    # O(n) - linear time
    def __str__(self):
        items = []
        current_item = self.left

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        
        return ', '.join(items)
    
    def append(self, value):
        new_node = Node(value)

        if self.right is None:
            self.left = self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        
        self.size += 1

    def appendleft(self, value):
        new_node = Node(value)

        if self.left is None:
            self.left = self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        
        self.size += 1
        

    def pop(self):
        if self.right is None:
            raise ValueError("queue is empty.")
        else:
            pop_value = self.right.value
            self.right = self.right.prev
            self.right.next = None
            self.size -= 1

            return pop_value

    def popleft(self):
        if self.left is None:
            raise ValueError("queue is empty.")
        else:
            pop_value = self.left.value
            self.left = self.left.next
            self.left.prev = None
            self.size -= 1

            return pop_value


if __name__ == "__main__":
    
    d = Deque()
    
    d.append(1)
    d.append(2)
    d.appendleft(3)
    print(d)

    d.pop()
    d.popleft()
    print(d)