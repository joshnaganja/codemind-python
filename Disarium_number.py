n=int(input())
t=n
z=str(n)
l=len(z)
r=s=0
while n!=0:
    r=n%10
    s=s+int(r**l)
    n=n//10
    l=l-1
if s==t:
    print("True")
else:
    print("False")