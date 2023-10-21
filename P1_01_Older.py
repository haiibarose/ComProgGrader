p1 = [i.strip(',') for i in input().split()]
p2 = [i.strip(',') for i in input().split()]

month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
         'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
birth1 = [int(p1[3]), month[p1[1]], int(p1[2])]
birth2 = [int(p2[3]), month[p2[1]], int(p2[2])]

if birth1[0] > birth2[0]:
    print(p2[0])
elif birth1[0] < birth2[0]:
    print(p1[0])
else:
    if birth1[1] > birth2[1]:
        print(p2[0])
    elif birth1[1] < birth2[1]:
        print(p1[0])
    else:
        if birth1[2] > birth2[2]:
            print(p2[0])
        elif birth1[2] < birth2[2]:
            print(p1[0])
        else:
            print(p1[0], p2[0])