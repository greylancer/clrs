import random

def random_select(A, p, r, i):
    while p <= r:
        if p == r:
            return A[p]
        q = random_partition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q-1
        else:
            p = q+1
            i = i-q

def random_partition(A, p, r):
    i = random.randrange(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    j = p
    while j <= r - 1:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A = [2, 8, 7, 1, 3, 5, 6, 4]
ret = random_select(A, 0, len(A) - 1, 4)
print(ret)