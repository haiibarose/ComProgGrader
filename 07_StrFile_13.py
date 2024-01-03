signs = '''"'`~!@#$%^&*()_+-=[]|\;:,<.>/?\"'''
words = input().strip(signs).split()

for i in range(len(words)):
    for sign in signs:
        if sign in words[i]:
            words[i] = words[i].replace(sign, '')

    words[i] = words[i].capitalize()
print(words[0].lower()+''.join(words[1:]))