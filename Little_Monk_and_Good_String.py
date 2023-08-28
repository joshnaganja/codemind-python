s=input()
c=0
l=[]
for i in s:
    if i in "aeiou":
        c=c+1
        l.append(c)
    else:
        c=0
print(max(l))