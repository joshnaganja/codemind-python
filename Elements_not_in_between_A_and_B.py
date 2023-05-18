n=int(input())
l1=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in l:
    if i>=a and i<=b:
        pass
    else:
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    for i in l1:
        print(i,end=' ')