data = [int(i) for i in input().split()]
data = [data[0]] + data + [data[-1]]

count = 0
for i in range(1, len(data)-1):
    if data[i-1] < data[i] and data[i] > data[i+1]:
        count += 1
print(count)