n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
for i in l1:
    if i in l2:
        pass
    else:
        l3.append(i)
if len(l3)==0:
    print("-1")
else:
    for i in l3:
        print(i,end=' ')
        