n = int(input())
data = dict()
top = dict()
ans = 0
for i in range(n):
    name, price = input().split()
    data[name] = float(price)

m = int(input())
for i in range(m):
    name, count = input().split()
    if name in data:
        price = data[name]*int(count)
        if name in top:
            top[name] += price
        else:
            top[name] = price
        ans += price

if len(top) == 0:
    print('No ice cream sales')
else:
    mx = max(top.values())
    print(f"Total ice cream sales: {ans}")
    print(f"Top sales: {', '.join(sorted([key for key, value in top.items() if value==mx]))}")