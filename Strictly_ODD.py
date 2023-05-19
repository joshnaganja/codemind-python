n=int(input())
c1=0
c2=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]%2!=0 and i%2!=0:
        c1=c1+1
for i in range(len(l)):
    if i%2!=0:
        c2=c2+1
if c1==c2:
    print("True")
else:
    print("False")
        
    