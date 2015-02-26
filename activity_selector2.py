def activity_selector(s, f):
    if len(s) == 0 or len(s) != len(f):
        return None

    n = len(s)
    c = [[0 for x in range(n+2)] for x in range(n+2)]
    for L in range(1, n+2):
        for i in range(0, n+2-L):
            lo = i 
            hi = i + L
            max_num = 0
            for k in range(lo+1, hi):
                if lo == 0:
                    left = 0
                else:
                    left = f[lo-1]
                if hi == n+1:
                    right = float('inf')
                else:
                    right = s[hi-1]

                if s[k-1] >= left and f[k-1] <= right:
                    cur_num = c[lo][k] + c[k][hi] + 1
                    if cur_num > max_num:
                        max_num = cur_num
            c[lo][hi] = max_num

    return c[0][-1]

s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]
ret = activity_selector(s, f)
print(ret)
