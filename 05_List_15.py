number = [int(i) for i in input().split()]

ans = list()
for n in number:
    if (n not in ans):
        ans.append(n)
print(len(ans))
if (len(ans) >= 10):
    print(sorted(ans)[:10])
else:
    print(sorted(ans))