filename, year = input().split()
year = year[-2:]
file = open(filename, 'r')
scores = list()
for lines in file.readlines():
    # print(lines)
    id, score = lines.strip().split()
    if id[:2] == year:
        scores.append(float(score))
if len(scores) == 0:
    print('No data')
else:
    print(min(scores), max(scores), sum(scores)/len(scores))