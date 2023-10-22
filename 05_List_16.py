n = int(input())

ans = [str(n)]
while (n != 1):
    if (n % 2 == 0):
        n = n / 2  # ปัดเýþทิ้ง
    else:
        n = 3*n + 1
    ans.append(str(int(n)))
print('->'.join(ans[-15:]))