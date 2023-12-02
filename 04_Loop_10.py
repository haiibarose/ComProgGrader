a = float(input())

L = 0
U = a
c = 1
while U > 0:
    U /= 10
    c += 1
U = c
x = (L+U)/2
while abs(a-10**x) > 1e-10*max(a, 10**x):
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    x = (L+U)/2
print(round(x, 6))