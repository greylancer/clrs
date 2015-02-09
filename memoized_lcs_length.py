class LCS:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.c = [[-1 for y in Y] for x in X]
        for i in range(c):
            for j in range(c[0]):
                if i == 0 or j == 0:
                    c[i][j] = 0

    def memoized_lcs_length(self, i, j):
        if self.c[i][j] >= 0:
            return self.c[i][j]
        if self.X[i] == self.Y[j]:
            self.c[i][j] = memoized_lcs_length(i-1, j-1) + 1
            return self.c[i][j]
        else:
            self.c[i][j] = max(self.memoized_lcs_length(i, j-1), self.memoized_lcs_length(i-1, j))
            return self.c[i][j]