class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False           
        if self.front== -1:
                self.rear =0
                self.front=0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty(): 
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def get_front(self) -> int:
        if not self.is_empty():
            return self.queue[self.front]
        else:
            return -1

    def get_rear(self):
        if not self.is_empty():
            return self.queue[self.rear]
        else:
            return -1

    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False

    def is_full(self):
        if (self.front == 0 and self.rear == self.size-1) or self.front == (self.rear+1)%self.size:
            return True
        else:
            return False
