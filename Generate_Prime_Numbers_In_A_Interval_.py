def is_prime(n):
    c,f=0,0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        f=1
    return f
l=int(input())
u=int(input())
for i in range(l,u+1):
    if is_prime(i)==1:
        print(i)