n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in l:
    if i%2==0:
        c1=c1+i
    else:
        c2=c2+i
print(abs(c1-c2))