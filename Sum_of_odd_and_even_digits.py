n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in range(len(l)):
    if i%2==0:
        c1=c1+l[i]
    else:
        c2=c2+l[i]
c=c1-c2
if c==0:
    print("YES")
else:
    print("NO")