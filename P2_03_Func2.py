def convex_polygon_area(p):
    area = 1
    plus = 0
    minus = 0
    for i in range(len(p)):
        dot = p[i]
        if i % 2 == 0:
            x1 = dot[0]
            y1 = dot[1]
            if i >= 1:
                plus += x2*y1
                minus += x1*y2
        else:
            x2 = dot[0]
            y2 = dot[1]
            plus += x1*y2
            minus += x2*y1
    return abs((plus-minus)/2)


def is_heterogram(s):
    word = s.lower().replace(' ', '')
    return len(set(word.lower())) == len(word)


def replace_ignorecase(s, a, b):
    idx = s.lower().find(a.lower())
    length = len(a)
    while idx != -1:
        s = s[:idx]+b+s[idx+length:]
        idx = s.lower().find(a.lower(), idx+length+1)
    return s


def top3(votes):
    ans = list()
    if len(votes) <= 3:
        for i in sorted(votes.keys()):
            ans.append(i)
    else:
        for i in range(3):
            max_key = max(votes, key=votes.get)
            ans.append(max_key)
            votes.pop(max_key)
    return ans


for k in range(2):
    exec(input().strip())