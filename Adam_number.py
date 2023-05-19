n=int(input())
t=n
s=0
c=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
a=s*s
b=t*t
while a!=0:
    z=a%10
    c=c*10+z
    a=a//10
if b==c:
    print("True")
else:
    print("False")