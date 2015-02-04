class MaxHeap:
    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)
        self.build()

    def heapify(self, i):
        while 2 * i + 1 < self.heap_size:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < self.heap_size and self.A[l] > self.A[i]:
                largest = l
            if r < self.heap_size and self.A[r] > self.A[largest]:
                largest = r

            if largest != i:
                self.A[largest], self.A[i] = self.A[i], self.A[largest]
                i = largest
            else:
                break

    def build(self):
        i = self.heap_size // 2 - 1
        while i >= 0:
            self.heapify(i)
            i -= 1

    @staticmethod
    def heap_sort(A):
        max_heap = MaxHeap(A)
        print(A)
        i = len(A) - 1
        while i >= 1:
            A[i], A[0] = A[0], A[i]
            max_heap.heap_size -= 1
            max_heap.heapify(0)

            i -= 1

A = [4, 1, 32, 16, 9, 14, 8, 7]
MaxHeap.heap_sort(A)
print(A)


