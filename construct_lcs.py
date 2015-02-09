def construct_lcs(c, X, Y):
    ret = []
    i = len(X) - 1
    j = len(Y) - 1
    while i >= 0 and j >= 0:
        if c[i][j] == 0:
            break
        if X[i] == Y[j]:
            i -= 1
            j -= 1
            ret.append(X[i])
        elif i - 1 >= 0 and c[i][j] == c[i-1][j]:
            i -= 1
        elif j - 1 >= 0 and c[i][j] == c[i][j-1]:
            j -= 1
        else:
            break

    ret.reverse()
    return ret

