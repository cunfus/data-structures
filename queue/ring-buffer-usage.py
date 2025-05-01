import time
import random
import os

class RingBuffer:
    def __init__(self, capacity, overwrite=True):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.overwrite = overwrite

    def enqueue(self, value):
        if self.size == self.capacity:
            if not self.overwrite:
                return False
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

        self.buffer[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def current_state(self):
        return [self.buffer[(self.front + i) % self.capacity] for i in range(self.size)]

# 清屏函数，兼容 Windows / Unix
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 打印文本条形图
def print_bar_chart(data):
    for value in data:
        bar = '█' * int((value - 15) * 3)  # 放大比例
        print(f"Temp: {value:4.1f} | {bar}")

if __name__ == "__main__":
        
    buffer = RingBuffer(5)

    while True:
        temp = round(20 + random.uniform(-2, 2), 1)
        buffer.enqueue(temp)

        clear_screen()
        print("实时温度流（最近 5 条）")
        print_bar_chart(buffer.current_state())

        time.sleep(1)
