def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    for row in range(len(A)):
        for col in range(len(A[0])):
            A[row][col] *= c
    return A

def mult(A, B):
    ans = [list([0 for i in range(len(B[0]))]) for j in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B[0])):
            for j in range(len(B)):
                ans[i][k] += A[i][j]*B[j][k]
            
    return ans

exec(input().strip())