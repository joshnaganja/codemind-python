def is_prime(n):
    c,f=0,0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        f=1
    return f
n=int(input())
t=n
r,c,d=0,0,0
while n!=0:
    r=n%10
    d=d+1
    if is_prime(r)==1:
        c=c+1
    n=n//10
if is_prime(t)==1 and c==d:
    print("Mega Prime")
else:
    print("Not Mega Prime")