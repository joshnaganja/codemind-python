def isugly(n):
    if n>0:
        factors=[2,3,5]
        for i in factors:
            while n%i==0:
                n=n//i
        return n==1
    else:
        return False
n=int(input())
if isugly(n)==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")