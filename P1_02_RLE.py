encode = input()

if(encode=='str2RLE'):
    code = input()

    ch = str()
    count = 0
    for i in range(len(code)):
        if(ch==code[i]):
            count += 1
        else:
            if(count!=0):
                print(ch, count, end=' ')
            ch = code[i]
            count = 1
    print(ch, count)
elif(encode=='RLE2str'):
    code = input().split()

    for i in range(0, len(code), 2):
        print(code[i]*int(code[i+1]), end='')
else:
    print('Error')