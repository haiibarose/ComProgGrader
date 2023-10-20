import math

up_1 = math.pi
up_2 = math.factorial(10)/8**8
up_3 = math.log(9.7, math.e)
power = 7/math.sqrt(71) - math.sin(math.radians(40))

up = up_1 - up_2 + up_3**power
down = (1.2)**(2.3**(1/3))
ans = up/down
print(round(ans, 6))