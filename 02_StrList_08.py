import math

a, b, c = [i if i.strip() else '0' for i in input().split(',')]
# decimal to fraction
numerator = int(b+c)-int(b)
denominator = int('9'*len(c)+'0'*(0 if b == '0' else len(b)))
gcd = math.gcd(numerator, denominator)

print(f'{(int(a)*denominator+numerator)//gcd} / {denominator//gcd}')