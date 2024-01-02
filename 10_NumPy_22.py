import numpy as np

def mult_table(nrows, ncols):
    r = np.arange(1, nrows+1)
    c = np.arange(1, ncols+1)
    mt = np.outer(r, c)
    return mt

exec(input().strip())