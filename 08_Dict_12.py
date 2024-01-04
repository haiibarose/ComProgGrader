n = int(input())
key_name = dict()
key_nickname = dict()
for i in range(n):
    name, nickname = input().split()
    key_name[name] = nickname
    key_nickname[nickname] = name
m = int(input())
for i in range(m):
    search = input()
    if search in key_name:
        print(key_name[search])
    elif search in key_nickname:
        print(key_nickname[search])
    else:
        print('Not found')