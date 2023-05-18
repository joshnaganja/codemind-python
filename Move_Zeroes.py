n=int(input())
l1=[]
c=0
l=list(map(int,input().split()))
for i in l:
    if i==0:
        c+=1
    else:
        l1.append(i)

for i in range(c):
    l1.append(0)
for i in l1:
    print(i,end=' ')