n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        c=c+1
if c==n:
    print("True")
else:
    print("False")