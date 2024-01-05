n = int(input())
data = list()
for i in range(n):
    info = input().split()
    data.append(info)
search = input().split()
for value in data:
    yes = True
    for s in search:
        if s not in value:
            yes = False
    if yes:
        print(' '.join(value))