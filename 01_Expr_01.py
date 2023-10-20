import math

n = int(input())
lower = math.sqrt(2*math.pi) * n**(n+1/2) * math.exp(-n+1/(12*n+1))
upper = math.sqrt(2*math.pi) * n**(n+1/2) * math.exp(-n+1/(12*n))

print(lower)
print(upper)