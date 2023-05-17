n=int(input())
a=int(n**0.5)
for i in range(2,a+1):
    if n%i==0:
        print("not a prime")
        break
else:
        print("prime")
        