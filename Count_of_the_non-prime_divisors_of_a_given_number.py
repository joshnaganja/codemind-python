def is_prime(n):
    c,f=0,0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        f=1
    return f
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
d=0
for i in l:
    if is_prime(i)==0:
        d=d+1
print(d)