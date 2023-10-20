u = [float(i) for i in input().strip('[]').split(',')]
v = [float(i) for i in input().strip('[]').split(',')]

ans = [u[0]+v[0], u[1]+v[1], u[2]+v[2]]
print(str(u), '+', str(v), '=', str(ans))