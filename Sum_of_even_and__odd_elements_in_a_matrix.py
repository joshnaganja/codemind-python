r,c=map(int,input().split())
mat=[]
s=0
s1=0
for i in range(r):
        lst=list(map(int,input().split()))
        mat.append(lst)
for i in mat:
    for j in i:
        if(j%2==0):
            s=s+j
        else:
            s1=s1+j
print(s,s1)