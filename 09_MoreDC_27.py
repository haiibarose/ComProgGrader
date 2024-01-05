def knows(R, x, y):
    # return True if x knows y
    return y in R[x]

def is_celeb(R, x):
    # return True if a is celeb, otherwise return False
    # return False if x knows someone who is not him/herself
    # return False if there exists someone in R who don't know x
    # otherwise return True
    if len(R[x]) != 0:
        return False
    for people in R:
        if (people != x) and (not knows(R, people, x)):
            return False
    return True

def find_celeb(R):
    # for each person x in the party
    # if x is celeb --> return x
    # if no celeb in the party --> return None
    for people in R:
        if is_celeb(R, people):
            return people
    return None

def read_relations():
    # build a dictionary R from inputs
    # whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[0] not in R:
            R[d[0]] = set()
        if d[1] not in R:
            R[d[1]] = set()
        R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())  # do not remove this line