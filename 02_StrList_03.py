d, m, y = input().split('/')

year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
print(year[int(m)-1], d+',', y)