n = int(input())
teams = set()
lose = set()
for i in range(n):
    win, los = input().split()
    teams = teams.union({win, los})
    lose = lose.union({los})
winner = teams.difference(lose)
print(sorted(winner))