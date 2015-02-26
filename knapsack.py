def knapsack(W, val, wt):
    if W <= 0 or len(val) == 0 or len(val) != len(wt):
        return 0

    n = len(val)
    c = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(0, n+1):
        for w in range(0, W+1):
            if i == 0 or w == 0:
                c[i][w] = 0
            elif w >= wt[i-1]:
                c[i][w] = max(c[i-1][w], c[i-1][w-wt[i-1]] + val[i-1])
            else:
                c[i][w] = c[i-1][w]

    return c[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
ret = knapsack(50, val, wt)
print(ret)
