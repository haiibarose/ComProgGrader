n = int(input())
data = dict()
for i in range(n):
    name, singer, cate, time = [x.strip() for x in input().split(',')]
    m = time.split(':')[0]
    s = time.split(':')[1]
    second = int(m)*60 + int(s)
    if cate not in data:
        data[cate] = second
    else:
        data[cate] += second
ans = list()
for key, value in data.items():
    ans.append([value,key])
ans.sort(reverse=True)
idx = 0
while True:
    if (idx>=len(ans)) or (idx>=3):
        break
    second, name = ans[idx]
    minute = second//60
    second -= minute*60
    if len(str(second))==1:
        print(f"{name} --> {minute}:0{second}")
    else:
        print(f"{name} --> {minute}:{second}")
    idx += 1