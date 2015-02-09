def activity_selector(s, f, v):
    if len(s) == 0 or len(s) != len(f) or len(s) != len(v):
        return None

    n = len(s)
    c = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        c[i][i] = v[i]

    for l in range(1, n):
        for i in range(0, n-1):
            lo = i
            hi = i + l
            for k in range(lo, hi):
                if 