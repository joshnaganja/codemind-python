def fun(n):
    t=n
    f,d,c=0,0,0
    while n!=0:
        r=n%10
        d=d+1
        if r!=0 and t%r==0:
            c=c+1
        n=n//10
    if c==d:
        f=1
    return f
l=int(input())
u=int(input())
for i in range(l,u+1):
    if fun(i)==1:
        print(i,end=" ")