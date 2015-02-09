class DListNode:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None

    @staticmethod
    def search(self, head, k):
        i = head
        while not i and i.key != k:
            i = i.next
        return i

    @staticmethod
    def insert(self, head, x):
        x.next = head
        x.prev = None
        if not head:
            head.prev = x
        return x




