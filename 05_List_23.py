import math

n = int(input())
d = list()
for i in range(n):
    x, y = [float(i) for i in input().split()]
    d.append((math.sqrt(x**2 + y**2), i+1, x, y))
d.sort()
print(f'#{d[2][1]}: ({d[2][2]}, {d[2][3]})')