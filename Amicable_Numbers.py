a=int(input())
b=int(input())
c1=0
c2=0
for i in range(1,a):
    if a%i==0:
        c1=c1+i
for i in range(1,b):
    if b%i==0:
        c2=c2+i
if c1==b and c2==a:
    print("Amicable")
else:
    print("Not Amicable")