class Node:

    def __init__(self, value):
        self.value = value
        self.min = value
        self.max = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    # O(1) - constant time
    def __len__(self):
        return self.size

    # O(n) - linear time
    def __str__(self):
        items = []
        current_item = self.top
 
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
     
        return ', '.join(items[::-1])
 
    # O(1) - constant time
    def push(self, value):
        new_node = Node(value)
        if self.top is not None:
            if self.top.max > value:
                new_node.max = self.top.max
            if self.top.min < value:            
                new_node.min = self.top.min

        new_node.next = self.top
        self.top = new_node

        self.size += 1

        # for debugging
        print(f"Node: value = {new_node.value}, max = {new_node.max} min = {new_node.min}")

    # O(1) - constant time
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        else:
            pop_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return pop_value

    # O(1) - constant time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value
    
    def is_empty(self):
        return self.size == 0
    
    def get_max(self):
        return self.top.max
    
    def get_min(self):
        return self.top.min
    


if __name__ == '__main__':
    stack = Stack()

    stack.push(3)    
    stack.push(2)
    stack.push(13)
    stack.push(5)
    stack.push(8)
    stack.push(1)