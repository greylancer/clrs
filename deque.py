class Queue:
    def __init__(self, n):
        self.A = n * [0]
        self.head = 0
        self.tail = 0

    def append(self, x):
        next_tail = (self.tail + 1) % len(self.A)
        if next_tail == self.head:
            raise Exception('Queue overflow')
        else:
            self.A[self.tail] = x
            self.tail = next_tail

    def appendleft(self, x):
        if self.head == 0:
            next_head = len(self.A) - 1
        else:
            next_head = self.head - 1
        if next_head == self.tail:
            raise Exception('Queue overflow')
        self.A[next_head] = x
        self.head = next_head

    def pop(self):
        if self.head == self.tail:
            raise Exception('Queue empty')
        if self.tail == 0:
            next_tail = len(self.A) - 1
        else:
            next_tail = self.tail - 1
        x = self.A[next_tail]
        self.tail = next_tail

        return x

    def popleft(self):
        if self.head == self.tail:
            raise Exception('Queue empty')
        next_head = (self.head + 1) % len(self.A)
        x = self.A[self.head]
        self.head = next_head

        return x

q = Queue(2)
q.appendleft(1)
print(q.pop())