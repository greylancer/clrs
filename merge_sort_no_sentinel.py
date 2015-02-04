def merge_sort(A):
    merge_sort_func(A, 0, len(A) - 1)

def merge_sort_func(A, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_func(A, start, mid)
    merge_sort_func(A, mid + 1, end)
    merge(A, start, mid, end)

def merge(A, start, mid, end):
    L = list(A[start:mid+1])
    R = list(A[mid+1:end+1])

    k = start
    i = 0
    j = 0
    while k <= end:
        if i >= mid - start + 1:
            A[k] = R[j]
            j += 1
        elif j >= end - mid:
            A[k] = L[i]
            i += 1
        elif L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

A = [2, 4, 5, 7, 1, 2, 3, 6]
merge_sort(A)
print(A)