def row_number(t, e):  # return row number of t containing e􀇰 (top row is row #0)
    for row in range(len(t)):
        if e in t[row]:
            return row

def flatten(t):  # return a list of ints converted from list of lists of ints t
    t = sum(t, [])
    t.remove(0)
    return t

def inversions(x):  # return the number of inversions of list x
    ans = 0
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                ans += 1
    return ans

def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    inver = inversions(t)
    zero = row_number(t, 0)
    if len(t) % 2 == 1 and inver % 2 == 0:
        return True
    else:
        if inver % 2 == 0 and zero % 2 == 1:
            return True
        elif inver % 2 == 1 and zero % 2 == 0:
            return True
    return False

exec(input().strip())  # do not remove this line