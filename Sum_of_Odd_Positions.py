n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2!=0:
        c=c+l[i]
print(c)