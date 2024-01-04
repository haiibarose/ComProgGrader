n = int(input())
union = set()
intersect = set()
st = True
for i in range(n):
    num = set(input().split())
    if st:
        union = set(num)
        intersect = set(num)
        st = False
    union = union.union(num)
    intersect = intersect.intersection(num)
print(len(union))
print(len(intersect))