n = int(input())
key_id = dict()
key_place = dict()
for i in range(n):
    id, places = input().split(':')
    for place in places.split(','):
        place = place.strip()
        if place not in key_place:
            key_place[place] = [id]
        else:
            key_place[place].append(id)
        if id not in key_id:
            key_id[id] = [place]
        else:
            key_id[id].append(place)
search = input()
ans = list()
for value in key_id[search]:
    for id in key_place[value]:
        if id not in ans:
            ans.append(id)

ans.remove(search)
if len(ans) == 0:
    print('Not Found')
else:
    print('\n'.join(ans))