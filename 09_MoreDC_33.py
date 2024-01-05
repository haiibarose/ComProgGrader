def add_poly(p1, p2):
    ans = list()
    idx1 = 0
    idx2 = 0
    while True:
        if (idx1 >= len(p1)) and (idx2 >= len(p2)):
            break
        if idx1 >= len(p1):
            ans.append(p2[idx2])
            idx2 += 1
        elif idx2 >= len(p2):
            ans.append(p1[idx1])
            idx1 += 1
        else:
            a1, b1 = p1[idx1]
            a2, b2 = p2[idx2]
            if b1 == b2:
                if a1+a2 != 0:
                    ans.append((a1+a2, b1))
                idx1 += 1
                idx2 += 1
            elif b1 > b2:
                ans.append((a1, b1))
                idx1 += 1
            else:
                ans.append((a2, b2))
                idx2 += 1
    return ans


def mult_poly(p1, p2):
    ans = list()
    for idx1 in range(len(p1)):
        a1, b1 = p1[idx1]
        for idx2 in range(len(p2)):
            a2, b2 = p2[idx2]
            ans.append((a1*a2,b1+b2))
    ans = add_poly(ans[:len(ans)//2], ans[len(ans)//2:])
    return ans


for i in range(3):
    exec(input().strip())
