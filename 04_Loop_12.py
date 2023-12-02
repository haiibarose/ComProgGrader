N = int(input())

left = list()
right = list()
for i in range(N):
    if i % 2 == 0:
        st, nd = [int(x) for x in input().split()]
    else:
        nd, st = [int(x) for x in input().split()]
    left.append(st)
    right.append(nd)
code = input()
if code == 'Zig-Zag':
    print(min(left), max(right))
else:
    print(min(right), max(left))