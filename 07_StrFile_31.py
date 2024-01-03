dna = input().strip()
operator = input().strip()
check = dna
valid = ['A', 'C', 'T', 'G']
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for ch in valid:
    check = check.upper().replace(ch, '')

if len(check) != 0:
    print('Invalid DNA')
else:
    if operator == 'R':
        ans = dna.lower()
        for ch in valid:
            ans = ans.replace(ch.lower(), complement[ch])
        print(ans[::-1])

    elif operator == 'F':
        ans = dict()
        for seq in valid:
            ans[seq] = dna.upper().count(seq)
        print(f"A={ans['A']}, T={ans['T']}, G={ans['G']}, C={ans['C']}")

    elif operator == 'D':
        i = -1
        ans = 0
        recheck = input().strip()
        while True:
            i = dna.upper().find(recheck, i+1)
            if i == -1:
                break
            ans += 1
        print(ans)