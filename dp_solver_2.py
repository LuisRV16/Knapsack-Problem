import numpy as np

def solve(v, w, W):
    n = len(v)
    c = np.zeros((n + 1, W + 1), dtype=int)
    
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j < w[i - 1]:
                c[i, j] = c[i - 1, j]
            else:
                c[i, j] = max(c[i - 1, j], v[i - 1] + c[i - 1, j - w[i - 1]])
    
    return c[n, W]
