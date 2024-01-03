while True:
    sentence = input()
    ans = ''
    if sentence == 'end':
        break
    for i in range(len(sentence)):
        asc = ord(sentence[i])
        if 65 <= asc <= 77:
            ans += chr(asc+13)
        elif 78 <= asc <= 90:
            ans += chr(asc-13)
        elif 97 <= ord(sentence[i]) <= 109:
            ans += chr(asc+13)
        elif 110 <= ord(sentence[i]) <= 122:
            ans += chr(asc-13)
        else:
            ans += chr(asc)
    print(ans)