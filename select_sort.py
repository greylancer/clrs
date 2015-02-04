def select_sort(A):
    if len(A) <= 1:
        return

    i = 0
    while i < len(A) - 1:
        min_index = i
        j = i + 1
        while j < len(A):
            if A[j] < A[min_index]:
                min_index = j
            j += 1

        if i != min_index:
            A[i], A[min_index] = A[min_index], A[i]
        i += 1

A = [5, 2, 4, 6, 1, 3]
select_sort(A)
print(A)
