n = [int(i) for i in input()]

n_12 = (11-(13*n[0]+12*n[1]+11*n[2]+10*n[3]+9*n[4]+8*n[5]+7*n[6]+6*n[7]+5*n[8]+4*n[9]+3*n[10]+2*n[11]) % 11) % 10
print(n[0], ''.join(map(str, n[1:5])), ''.join(map(str, n[5:10])), ''.join(map(str, n[10:12])), n_12, sep=' ')