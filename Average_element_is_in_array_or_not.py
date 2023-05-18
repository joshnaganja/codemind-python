n=int(input())
c=0
l=list(map(int,input().split()))
a=sum(l)
b=a//n
for i in l:
    if i==b:
        c=1
if c==1:
    print("True")
else:
    print("False")
    