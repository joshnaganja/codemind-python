n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
l1=[]
m=max(d.values())
for k,v in d.items():
    if v==m:
        c=c+1
        l1.append(k)
if c>1:
    print(min(l1))
else:
    for k,v in d.items():
        if v==max(d.values()):
            a=print(k)
            break

    