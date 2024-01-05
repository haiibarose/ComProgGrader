data = dict()
while True:
    code = input()
    if code=='q':
        break
    name, cate = [i.strip() for i in code.split(',')]
    if cate not in data:
        data[cate] = [name]
    else:
        data[cate].append(name)
for animal in data:
    print(f"{animal}: {', '.join(data[animal])}")