h = int(input())
n = 2*h-1

for i in range(h):
    for j in range(n):
        if (i == h-1):
            print('*', end='')
        elif (j == h-1-i or j == h-1+i):
            print('*', end='')
        elif (j == h-1 and i == 0):
            print('*', end='')
        else:
            print(' ', end='')
    print()