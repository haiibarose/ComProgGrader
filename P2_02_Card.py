order = input()
cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'C': 1, 'D': 2, 'H': 3, 'S': 4}

for card in range(0, len(order)-2, 2):
    left = order[card:card+2]
    right = order[card+2:card+4]
    # print(left, right)
    score = cards[left[0]]-cards[right[0]]
    # print(score)
    if score == 0:
        score = cards[left[1]]-cards[right[1]]
    if score < 0:
        print(f"-{abs(score)}", end='')
    elif score > 0:
        print(f"+{score}", end='')
    else:
        print("0", end='')