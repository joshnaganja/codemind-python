n=int(input())
t=n
s=0
k=1
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
while(t!=0):
    z=t%10
    k=k*z
    t=t//10
print(k-s)