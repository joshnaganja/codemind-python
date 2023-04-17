r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
for i in range(r):
    for j in range(c):
        s=s+mat[i][j]
print(s)