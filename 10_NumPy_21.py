import numpy as np

def sum_2_rows(M):
    s = M[::2, :]+M[1::2, :]
    return s

def sum_left_right(M):
    m, n = M.shape
    s = M[:, :n//2]+M[:, n//2:]
    return s

def sum_upper_lower(M):
    m, n = M.shape
    s = M[:m//2, :]+M[m//2:, :]
    return s

def sum_4_quadrants(M):
    m, n = M.shape
    s = M[:m//2, :n//2] + M[:m//2, n//2:] + M[m//2:, :n//2] + M[m//2:, n//2:]
    return s

def sum_4_cells(M):
    m, n = M.shape
    s = M[::2, ::2] + M[::2, 1::2] + M[1::2, ::2] + M[1::2, 1::2]
    return s

def count_leap_years(years):
    year = years-543
    return np.sum(np.logical_or((year % 400 == 0), np.logical_and(year % 4 == 0, year % 100 != 0)))

exec(input().strip())