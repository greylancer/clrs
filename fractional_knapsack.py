def knapsack(W, val, wt):
    if W == 0 or len(val) == 0 or len(val) != len(wt):
        return 0

    n = len(val)
    vws = sorted(range(n), key=lambda k: val[k]/wt[k], reverse=True)
    print(vws)

    val_sum = 0
    left_w = W
    for i in vws:
        if left_w >= wt[i]:
            left_w -= wt[i]
            val_sum += val[i]
        elif left_w < wt[i]:
            val_sum += val[i] * left_w / wt[i]

    return val_sum

val = [60, 100, 120]
wt = [10, 20, 30]
ret = knapsack(50, val, wt)
print(ret)