filename1, filename2 = input().strip().split()

file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
data1 = file1.readlines()
data2 = file2.readlines()

ans = list()
idx1 = 0
idx2 = 0
while True:
    if idx1 >= len(data1) and idx2 >= len(data2):
        break
    elif idx1 >= len(data1):
        ans.append(data2[idx2].strip())
        idx2 += 1
    elif idx2 >= len(data2):
        ans.append(data1[idx1].strip())
        idx1 += 1
    else:
        id1, gpa1 = data1[idx1].strip().split()
        id2, gpa2 = data2[idx2].strip().split()
        fac1, fac2 = id1[-2:], id2[-2:]
        if fac1 < fac2:
            ans.append(data1[idx1].strip())
            idx1 += 1
        elif fac1 > fac2:
            ans.append(data2[idx2].strip())
            idx2 += 1
        else:
            if id1 <= id2:
                ans.append(data1[idx1].strip())
                idx1 += 1
            else:
                ans.append(data2[idx2].strip())
                idx2 += 1

print('\n'.join(ans))
file1.close()
file2.close()