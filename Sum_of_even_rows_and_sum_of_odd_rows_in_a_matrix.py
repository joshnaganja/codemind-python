r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
s=0
s1=0
for i in range(r):
    if(i%2==0):
        s=s+sum(mat[i])
    else:
        s1=s1+sum(mat[i])
print(f"{s} {s1}")