class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise IndexError
        x = self.head.val
        self.head = self.head.next
        return x

s = ListStack()
s.push(1)
print(s.pop())