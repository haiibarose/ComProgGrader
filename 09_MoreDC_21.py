def factor(N):
    prime = [num for num in range(2, N) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    ans = list()
    for p in prime:
        n = 0
        while N % p == 0:
            n += 1
            N /= p
        if n != 0:
            ans.append([p, n])
    return ans

exec(input().strip())