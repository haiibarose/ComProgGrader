h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
dt = t2 - t1
dh = dt // (60*60) % 24  # add % 24 to make sure it's in 24 hour format
dt -= dh * 60*60
dm = dt // 60 % 60  # add % 60 to make sure it's in 60 minute format
dt -= dm*60
ds = dt % 60  # add % 60 to make sure it's in 60 second format
print(str(dh)+":"+str(dm)+":"+str(ds))