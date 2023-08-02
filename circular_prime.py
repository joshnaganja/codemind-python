def is_prime(n):
    c,f=0,0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        f=1
    return f
n=int(input())
s=0
t=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if is_prime(t)==1 and is_prime(s)==1:
    print("circular prime")
elif is_prime(t)==1 and is_prime(s)!=1:
    print("prime but not a circular prime")
else:
    print("not prime")