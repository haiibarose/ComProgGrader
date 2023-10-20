a = float(input())
b = float(input())
c = float(input())

x_1 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
x_2 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)

print(round(x_1, 3), round(x_2, 3))