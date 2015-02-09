def countintg_sort(A, k):
    C = (k + 1) * [0]
    for v in A:
        C[v] += 1
    i = 1
    while i < len(C):
        C[i] += C[i-1]
        i += 1

    B = len(A) * [0]
    i = len(A) - 1
    while i >= 0:
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
        i -= 1

    return B

A = [2, 5, 3, 0, 2, 3, 0, 3]
B = countintg_sort(A, 5)
print(B)
