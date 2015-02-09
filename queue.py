class Queue:
    def __init__(self, n):
        self.A = n * [0]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        next_tail = (self.tail + 1) % len(self.A)
        if next_tail == self.head:
            raise Exception('Queue overflow')
        else:
            self.A[self.tail] = x
            self.tail = next_tail

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('Queue empty')
        next_head = (self.head + 1) % len(self.A)
        x = self.A[self.head]
        self.head = next_head

        return x

q = Queue(2)
q.enqueue(1)
print(q.dequeue())

