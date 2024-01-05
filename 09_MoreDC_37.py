n = int(input())
data = dict()
for i in range(n):
    major, num = input().split()
    data[major] = int(num)

rank = list()
m = int(input())
for i in range(m):
    line = input().split()
    id = line[0]
    score = float(line[1])
    major = line[2:]
    rank.append([score, id, major])

rank.sort(reverse=True)
ans = list()
for score, id, majors in rank:
    for major in majors:
        if data[major] > 0:
            data[major] -= 1
            ans.append([id, major])
            break
ans.sort()
for id, major in ans:
    print(id, major)