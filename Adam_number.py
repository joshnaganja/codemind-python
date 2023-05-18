n=int(input())
t=n
s=0
z=0
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
a=s*s
b=t*t
while(a!=0):
    c=a%10
    z=z*10+c
    a=a//10
if z==b:
    print("True")
else:
    print("False")