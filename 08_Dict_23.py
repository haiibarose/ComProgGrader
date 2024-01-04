n = int(input())
key_name = dict()
key_phone = dict()
for i in range(n):
    inp = input().split()
    name, phone = ' '.join(inp[:2]), inp[-1]
    key_name[name] = phone
    key_phone[phone] = name
m = int(input())
for i in range(m):
    search = input()
    if search in key_name:
        print(f"{search} --> {key_name[search]}")
    elif search in key_phone:
        print(f"{search} --> {key_phone[search]}")
    else:
        print(f"{search} --> Not found")