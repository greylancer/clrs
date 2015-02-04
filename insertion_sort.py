def insertion_sort(A):
    if not A or len(A) <= 1:
        return

    i = 1
    while i < len(A):
        cur = A[i]
        j = i - 1
        while j >= 0 and A[j] > cur:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = cur

        i += 1


A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print(A)