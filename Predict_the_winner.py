import math
n=int(input())
l=list(map(int,input().split()))
s=0
t=0
for i in range(0,int(n//2)+1):
    s=s+l[i]
for i in range(int(n//2)+1,n):
    t=t+l[i]
b=s-t
a=abs(b)
if a%4==0:
    print("X")
else:
    print("Y")