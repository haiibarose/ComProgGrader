def is_odd(n):
    return n % 2 == 1


def has_odds(x):
    for i in x:
        if is_odd(i):
            return True
    return False


def all_odds(x):
    for i in x:
        if not is_odd(i):
            return False
    return True


def no_odds(x):
    if not has_odds(x):
        return True
    return False


def get_odds(x):
    ans = list()
    for i in x:
        if is_odd(i):
            ans.append(i)
    return ans


def zip_odds(a, b):
    odd_a = get_odds(a)
    odd_b = get_odds(b)
    ans = list()
    for i in range(max(len(odd_a), len(odd_b))):
        if i < len(odd_a):
            ans.append(odd_a[i])
        if i < len(odd_b):
            ans.append(odd_b[i])
    return ans

exec(input().strip())