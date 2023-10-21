code = input()

ch = str()
count = 0
for i in range(len(code)):
    if (ch == code[i]):
        count += 1
    else:
        if (count != 0):
            print(ch, count, end=' ')
        ch = code[i]
        count = 1
print(ch, count)