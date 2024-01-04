def reverse(d):
    ans = dict()
    for key, value in d.items():
        ans[value] = key
    return ans

def keys(d, v):
    return [key for key, value in d.items() if value == v]

exec(input().strip())