text = input()

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
ans = list()
for i in number:
    if i not in text:
        ans.append(i)
if (len(ans) == 0):
    print('None')
else:
    print(','.join(ans))