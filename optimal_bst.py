def optimal_bst(keys, freq):
    if len(keys) == 0 or len(keys) != len(freq):
        return None

    n = len(keys)
    c = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        c[i][i] = freq[i]

    for i in range(2, n+1):
        for j in range(0, n-i+1):
            min_cost = float('inf')
            lo = j
            hi = j + i - 1
            for k in range(lo, hi+1):
                if k - 1 < lo:
                    cur_cost = c[k+1][hi]
                elif k + 1 > hi:
                    cur_cost = c[lo][k-1]
                else:
                    cur_cost = c[lo][k-1] + c[k+1][hi] 

                if cur_cost < min_cost:
                    min_cost = cur_cost

            for k in range(lo, hi+1):
                min_cost += freq[k]
            c[lo][hi] = min_cost

    return c[0][n-1]

keys = [10, 12, 20]
freq = [34, 8, 50]
ret = optimal_bst(keys, freq)
print(ret)
