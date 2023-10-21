a, b, c, d = [float(i) for i in input().split()]

mn = a
mx = a
if (b < mn):
    mn = b
if (c < mn):
    mn = c
if (d < mn):
    mn = d
if (b > mx):
    mx = b
if (c > mx):
    mx = c
if (d > mx):
    mx = d

avg = (a+b+c+d-mn-mx)/2
print(round(avg, 2))