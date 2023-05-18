n=int(input())
l2=[]
l1=list(map(int,input().split()))
for i in range(len(l1)):
    l2.append((l1[i]*l1[i]))
l2.sort()
for i in l2:
    print(i,end=' ')