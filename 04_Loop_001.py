p = float(input())

k = 1
t = 1
while ((1-t) < p):
    t *= (365-k)/365
    k += 1
print(k)
