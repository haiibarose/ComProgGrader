import math

def distance1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def distance2(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def distance3(c1, c2):
    d = distance2(c1[:2], c2[:2])
    overlap = c1[-1]+c2[-1] > d
    return d, overlap

def perimeter(points):
    length = 0
    i = -1
    while (i < len(points)-1):
        length += distance2(points[i], points[i+1])
        i += 1
    return length

exec(input().strip())