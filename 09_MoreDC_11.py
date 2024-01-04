n = int(input())
for i in range(n):
    code = input()
    clean_code = code.lstrip('.')
    count = (len(code) - len(clean_code))//2
    print('.'*count+clean_code)