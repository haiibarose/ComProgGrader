import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    s = data[:, 1:]*weight.T
    sum_each = np.sum(s, axis=1)
    mean = np.average(sum_each)
    ans = data[sum_each < mean, 0]
    if len(ans) == 0:
        print('None')
    else:
        ans = str(ans.tolist()).strip('[]')
        print(ans)

exec(input().strip())