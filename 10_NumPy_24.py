import numpy as np

def peak_indexes(x):
    left = np.concatenate((x[0:1], x[:-1]), axis=0)
    right = np.concatenate((x[1:], x[-1:]), axis=0)
    ans = np.logical_and(left < x, x > right)
    return np.where(ans)[0]

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())  # Don't remove this line