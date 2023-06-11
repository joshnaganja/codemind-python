a=int(input())
b=int(input())
c=0
c1=0
for i in range(1,a):
    if a%i==0:
        c=c+i
for i in range(1,b):
    if b%i==0:
        c1=c1+i
if c==b and c1==a:
    print("Amicable")
else:
    print("Not Amicable")