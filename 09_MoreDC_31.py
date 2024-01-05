def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    x = gcd(a,b)
    y = gcd(a,c)
    z = gcd(x,y)
    return z==1

def primitive_Pythagorean_triples(max_len):
    # [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25],
    # [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53],
    # [11, 60, 61], [16, 63, 65], [33, 56, 65]]
    triple = list()
    for a in range(1, max_len+1):
        for b in range(a, max_len+1):
            for c in range(b, max_len+1):
                pytha = a**2+b**2
                if c**2==pytha and is_coprime(a, b, c):
                    triple.append([a,b,c])
    return triple

exec(input().strip())