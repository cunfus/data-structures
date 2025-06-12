class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.size = 1
    
    # O(n) -linear time
    def __str__(self):
        items = []
        index = self.head.next
        while index is not None:
            items.append(index.value)
            index = index.next
        
        return ', '.join(map(str, items))

    # O(n) - linear time
    def __contains__(self, value):
        index = self.head.next
        while index is not None:
            if index.value == value:
                return True
            index = index.next

        return False

    def __len__(self):
        return self.size - 1


    def insert(self, value, index):
        if index > self.size:
            raise IndexError("insertion: index out of bounds.")

        iter = self.head
        while index > 1:
            iter, index = iter.next, index - 1

        new_node = Node(value)
        new_node.next = iter.next
        iter.next = new_node

        self.size += 1
    
    # O(n) - linear time
    def append(self, value):
        self.insert(value, self.size)

    # O(1) - constant time
    def appendleft(self, value):
        self.insert(value, 1)


    def delete(self, index):
        if index > self.size:
            raise IndexError("deletion: index out of bounds.")
        
        iter = self.head
        while index > 1:
            iter, index = iter.next, index - 1

        ret_value = iter.next.value
        iter.next = iter.next.next
        self.size -= 1

        return ret_value

    # O(n) - linear time 
    def pop(self):
        ret_value = self.delete(self.size - 1) # 找到前一个元素
        return ret_value
    
    # O(1) - constant time
    def popleft(self):
        ret_value = self.delete(1)
        return ret_value

if __name__ == '__main__':
    fibo = LinkedList()
    
    fibo.append(1)
    fibo.append(2)
    fibo.append(3)
    fibo.append(4)
    
    fibo.appendleft(5)    
    fibo.popleft()

    print(fibo)

    print(len(fibo))
    print(3 in fibo)
    print(7 in fibo)