data = input()
avg = 0
count = 0
while (data != 'q'):
    avg += float(data)
    count += 1
    data = input()
if (count == 0):
    print('No Data')
else:
    print(round(avg/count, 2))