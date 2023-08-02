def add(n):
    while 1:
        su,s=0,0
        while n!=0:
            r=n%10
            s=s+r
            n=n//10
        if s<10:
            su=s
            break
        else:
            n=s
    return su
n=int(input())
print(add(n))