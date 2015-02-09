class MinPriorityQueue:
    def __init__(self, A):
        self.A = A
        self.build()

    @property
    def heap_size(self):
        return len(self.A)

    def build(self):
        i = self.heap_size // 2 - 1
        while i >= 0:
            self.heapify(i)
            i -= 1

    def heapify(self, i):
        while i < self.heap_size // 2:
            left = 2 * i + 1
            right = 2 * i + 2
            min_index = i
            if A[left] < A[min_index]:
                min_index = left
            if right < self.heap_size and A[right] < A[min_index]:
                min_index = right

            if min_index != i:
                A[min_index], A[i] = A[i], A[min_index]
                i = min_index
            else:
                break

    def minimum(self):
        return self.A[0]

    def extract_min(self):
        min_value = self.A[0]
        self.A[0] = self.A[self.heap_size-1]
        del self.A[-1]
        self.heapify(0)

        return min_value

    def decrease_key(self, i, key):
        if key >= self.A[i]:
            return

        p = (i - 1) // 2
        while p >= 0:
            if self.A[p] > key:
                self.A[i] = self.A[p]
            else:
                break
            i = p
            p = (i - 1) // 2

        self.A[i] = key

    def insert(self, key):
        self.A.append(float('inf'))
        self.decrease_key(self.heap_size-1, key)

if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    q = MinPriorityQueue(A)
    print(q.A)
    q.insert(0)
    print(q.A)


