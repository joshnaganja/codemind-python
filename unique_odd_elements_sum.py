n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
b=[]
for i in l:
    if i not in a:
        a.append(i)
for i in a:
    if i%2!=0:
        b.append(i)
print(sum(b))