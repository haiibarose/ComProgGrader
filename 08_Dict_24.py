def text2keys(text):
    code = {' ': 0, 'a': 2, 'b': 22, 'c': 222, 'd': 3, 'e': 33, 'f': 333,
            'g': 4, 'h': 44, 'i': 444, 'j': 5, 'k': 55, 'l': 555,
            'm': 6, 'n': 66, 'o': 666, 'p': 7, 'q': 77, 'r': 777,
            's': 7777, 't': 8, 'u': 88, 'v': 888, 'w': 9, 'x': 99, 'y': 999, 'z': 9999}
    ans = list()
    for ch in text.lower():
        if ch in code:
            ans.append(str(code[ch]))
    return ' '.join(ans)

def keys2text(keys):
    code = {'0': ' ', '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = str()
    for ch in keys.split():
        num, count = ch[0], len(ch)
        ans += code[num][count-1]
    return ans

exec(input().strip())