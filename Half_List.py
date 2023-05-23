n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    if i>=n//2 and i<n:
        l1.append(l[i])
l2=l1[::-1]
for i in range(n):
    if i>=0 and i<n//2:
        l2.append(l[i])
for i in l2:
    print(i,end=' ')