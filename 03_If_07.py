subscribers = int(input())

if (subscribers < 1e3):
    print(subscribers)
elif (subscribers < 1e4):
    print(str(round(subscribers/1e3, 1)) + 'K')
elif (subscribers < 1e6):
    print(str(round(subscribers/1e3)) + 'K')
elif (subscribers < 1e7):
    print(str(round(subscribers/1e6, 1)) + 'M')
elif (subscribers < 1e9):
    print(str(round(subscribers/1e6)) + 'M')
elif (subscribers < 1e10):
    print(str(round(subscribers/1e9, 1)) + 'B')
else:
    print(str(round(subscribers/1e9)) + 'B')