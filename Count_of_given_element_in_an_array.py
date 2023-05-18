n=int(input())
c=0
l=list(map(int,input().split()))
n1=int(input())
for i in l:
    if n1==i:
        c=c+1
print(c)