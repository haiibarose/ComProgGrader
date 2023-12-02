ans = input().strip()
key = input().strip()

if len(ans) != len(key):
    print('Incomplete answer')
else:
    point = 0

    for i in range(len(ans)):
        if ans[i] == key[i]:
            point += 1
    print(point)