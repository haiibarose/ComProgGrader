p1 = [i for i in input().split()]
p2 = [i for i in input().split()]

for i in range(len(p1)):
    if p1[i] == 'A':
        p1[i] = 4
    elif p1[i] == 'B':
        p1[i] = 3
    elif p1[i] == 'C':
        p1[i] = 2
    elif p1[i] == 'D':
        p1[i] = 1
    elif p1[i] == 'F':
        p1[i] = 0

for i in range(len(p2)):
    if p2[i] == 'A':
        p2[i] = 4
    elif p2[i] == 'B':
        p2[i] = 3
    elif p2[i] == 'C':
        p2[i] = 2
    elif p2[i] == 'D':
        p2[i] = 1
    elif p2[i] == 'F':
        p2[i] = 0

p1_status = p1[2] == 4 and p1[3] >= 2 and p1[4] >= 2
p2_status = p2[2] == 4 and p2[3] >= 2 and p2[4] >= 2

if not (p1_status) and not (p2_status):
    print('None')

elif p1_status and p2_status:
    if float(p1[1]) > float(p2[1]):
        print(p1[0])
    elif float(p2[1]) > float(p1[1]):
        print(p2[0])
    elif p1[3] > p2[3]:   # equal GPAX -> compare cal1
        print(p1[0])
    elif p2[3] > p1[3]:
        print(p2[0])
    elif p1[4] > p2[4]:   # equal GPAX and equal cal1 -> compare cal2
        print(p1[0])
    elif p2[4] > p1[4]:
        print(p2[0])
    else:               # equal GPAX and equal cal1 and equal cal2 -> both
        print('Both')

elif p1_status:
    print(p1[0])
else:
    print(p2[0])