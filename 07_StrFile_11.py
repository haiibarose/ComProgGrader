word = input().strip()
if word[-1] in 'xs' or word[-2:] in ['ch']:
    ans = word+'es'
elif word[-1] in 'y' and word[-2] not in 'aeiou':
    ans = word[:-1]+'ies'
else:
    ans = word+'s'
print(ans)