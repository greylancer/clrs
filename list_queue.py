class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_code = ListNode(x)
        if self.tail:
            self.tail.next = new_code
        self.tail = new_code
        if not self.head:
            self.head = new_code

    def dequeue(self):
        if not self.head:
            raise IndexError
        x = self.head.val
        self.head = self.head.next
        return x

q = ListQueue()
q.enqueue(1)
print(q.dequeue())
