mn_left = 1e10
mx_left = -1e10
mn_right = 1e10
mx_right = -1e10
i = 0
while True:
    code = input()
    if code == 'Zig-Zag' or code == 'Zag-Zig':
        break
    if i % 2 == 0:
        st, nd = [int(x) for x in code.split()]
    else:
        nd, st = [int(x) for x in code.split()]
    if (st < mn_left):
        mn_left = st
    if (st > mx_left):
        mx_left = st
    if (nd < mn_right):
        mn_right = nd
    if (nd > mx_right):
        mx_right = nd
    i += 1

if code == 'Zig-Zag':
    print(mn_left, mx_right)
else:
    print(mn_right, mx_left)