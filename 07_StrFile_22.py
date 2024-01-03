st = input().lower().replace(' ', '')
nd = input().lower().replace(' ', '')

for i in st:
    nd = nd.replace(i, '', 1)

print('YES') if len(nd) == 0 else print('NO')