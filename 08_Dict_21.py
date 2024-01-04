word = input().lower()
ans = list()
char = set(word)
for ch in char:
    ans.append([-word.count(ch), ch])
for c, ch in sorted(ans):
    print(f"{ch} -> {-c}")