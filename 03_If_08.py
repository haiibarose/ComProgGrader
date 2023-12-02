d = int(input())
m = int(input())
y = int(input()) - 543

num = d
if m > 1:
    num += 31
if m > 2:
    num += 28
    if (y % 400 == 0) or (y % 4 == 0) and (y % 100 != 0):
        num += 1
if m > 3:
    num += 31
if m > 4:
    num += 30
if m > 5:
    num += 31
if m > 6:
    num += 30
if m > 7:
    num += 31
if m > 8:
    num += 31
if m > 9:
    num += 30
if m > 10:
    num += 31
if m > 11:
    num += 30

print(num)