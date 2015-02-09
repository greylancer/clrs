def cal(p):
    if len(p) <= 2:
        return 0
    n = len(p) - 1
    c = [[0 for x in range(n)] for x in range(n)]

    for L in range(1, n):
        for i in range(0, n-L):
            lo = i
            hi = i + L
            min_cost = float('inf')
            for k in range(lo, hi):
                cur_cost = c[lo][k] + c[k+1][hi] + p[lo]*p[k+1]*p[hi+1]
                if cur_cost < min_cost:
                    min_cost = cur_cost
            c[lo][hi] = min_cost

    return c[0][n-1]

p = [40, 20, 30, 10, 30]
ret = cal(p)
print(ret)
