def inversion_sum(A):
    return inversion_sum_func(A, 0, len(A) - 1)

def inversion_sum_func(A, start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2
    num1 = inversion_sum_func(A, start, mid)
    num2 = inversion_sum_func(A, mid + 1, end)
    num3 = merge(A, start, mid, end)
    return num1 + num2 + num3

def merge(A, start, mid, end):
    L = list(A[start:mid+1])
    R = list(A[mid+1:end+1])
    
    inver_sum = 0

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
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            inver_sum += mid - start + 1 - i
            j += 1
        k += 1

    return inver_sum

A = [2, 3, 8, 6, 1]
ret = inversion_sum(A)
print(ret)