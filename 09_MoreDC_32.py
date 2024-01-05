def first_fit(L, e): # นำ e ใส่รำยกำรย่อยใน L ดว้ ยวิธี first fit
    for idx in range(len(L)):
        if sum(L[idx])+e<=100:
            L[idx].append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e): # นำ e ใส่รำยกำรย่อยใน L ดว้ ยวิธี best fit
    mx = [-1,0,0]
    for idx in range(len(L)):
        if sum(L[idx])+e<=100:
            if sum(L[idx])+e>mx[1]:
                mx = [idx,sum(L[idx])+e,e]
    if mx[0]==-1:
        L.append([e])
    else:
        L[mx[0]].append(mx[2])
    return L

def partition_FF(D): # คนื ลสิ ต์ของลสิ ต์ทไี่ ดจ้ ำกกำรแบ่งขอ้ มูลใน D ดว้ ย first fit
    ans = list()
    for data in D:
        ans = first_fit(ans, data)
    return ans

def partition_BF(D): # คนื ลสิ ต์ของลสิ ต์ทไี่ ดจ้ ำกกำรแบ่งขอ้ มูลใน D ดว้ ย best fit
    ans = list()
    for data in D:
        ans = best_fit(ans, data)
    return ans

exec(input().strip())