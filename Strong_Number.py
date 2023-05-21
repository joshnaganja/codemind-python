s=0
n=int(input())
t=n
while(n):
    i=1
    fact=1
    r=n%10
    while(i<=r):
        fact=fact*i
        i=i+1
    s=s+fact
    n=n//10
if(s==t):
    print(f"The number {t} is a strong number")
else:
    print(f"The number {t} is not a strong number")