n = int(input())

ans = list()
data = list()
for i in range(n):
    data.append(int(input()))

data+=[int(i) for i in input().split()]  # Changed append to extend

while True:
    num = int(input())
    if num == -1:
        break
    data.append(num)

for i in range(len(data)):
    if i % 2 == 0:
        ans.append(data[i])
    else:
        ans.insert(0, data[i])
    i += 1
print(ans)