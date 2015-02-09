def activity_selector(s, f):
    if len(s) == 0 or len(s) != len(f):
        return None

    pre_f = 0
    selectors = []
    for i in range(len(f)):
        if s[i] >= pre_f:
            selectors.append(i)
            pre_f = f[i]

    return selectors