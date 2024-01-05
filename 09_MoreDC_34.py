def pattern1(nrows, ncols):
    ans = [[0 for i in range(ncols)] for j in range(nrows)]
    value = 1
    for i in range(nrows):
        for j in range(ncols):
            ans[i][j] += value
            value += 1
    return ans

def pattern2(nrows, ncols):
    ans = [[0 for i in range(ncols)] for j in range(nrows)]
    value = 1
    for j in range(ncols):
        for i in range(nrows):
            ans[i][j] += value
            value += 1
    return ans

def pattern3(N):
    ans = [[0 for i in range(N)] for j in range(N)]
    value = 1
    for i in range(N):
        for j in range(N):
            if i >= j:
                ans[i][j] += value
                value += 1
    return ans

def pattern4(N):
    ans = [[0 for i in range(N)] for j in range(N)]
    value = 1
    for j in range(N):
        for i in range(N-1, -1, -1):
            if i <= j:
                ans[i][j] += value
                value += 1
    return ans

def pattern5(N):
    ans = [[0 for i in range(N)] for j in range(N)]
    value = 1
    for j in range(N):
        i = 0
        while True:
            ans[i][j] += value
            value += 1
            i += 1
            j += 1
            if i >= N or j >= N:
                break
    return ans

def pattern6(N):
    ans = [[0 for i in range(N)] for j in range(N)]
    value = 1
    i = 0
    j = 0
    forward = True
    for _ in range(N):
        while True:
            ans[i][j] += value
            value += 1
            if forward:
                i += 1
                j += 1
            else:
                i -= 1
                j -= 1
            if i >= N or j >= N:
                forward = False
                i -= 2
                j = N - 1
                break
            if i < 0 or j < 0:
                forward = True
                i = 0
                j += 2
                break
    return ans

exec(input().strip())