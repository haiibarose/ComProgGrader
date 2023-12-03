cards = input().split()
codes = input()

for code in codes:
    st = cards[:len(cards)//2]
    nd = cards[len(cards)//2:]
    if code == 'C':
        cards = nd + st
    elif code == 'S':
        cards = list()
        for i in range(len(st)):
            cards.append(st[i])
            cards.append(nd[i])

print(' '.join(cards))