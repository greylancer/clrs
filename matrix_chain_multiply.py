def cal(A, s, i, j):
    if i == j:
        return A[i]

    k = s[i][j]
    L = cal(A, s, i, k)
    R = cal(A, s, k+1, j)
    if len(L[0]) != len(R):
        raise Exception('Not compatible')
    X = [[0 for x in range(len(R[0]))] for x in range(len(L))]

    for i in range(len(L)):
        for j in range(len(R[0])):
            x = 0
            for k in range(len(L[0])):
                x += L[i][k] * R[k][j]
            X[i][j] = x

    return X
