def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    j = p
    while j <= r-1:
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

A = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(A, 0, len(A) - 1)
print(A)

