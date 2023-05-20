import math
def is_integer(x):
    if x>=0:
        sr=int(math.sqrt(x))
        return (sr*sr)==x
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if is_integer(i):
        c=c+i
    else:
        pass
print(c)