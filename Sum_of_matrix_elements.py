r1=int(input())
c1=int(input())
a=[]
b=[]
for i in range(r1):
    l=list(map(int,input().split()))
    a.append(l)
    j=sum(l)
    b.append(j)
print(sum(b))