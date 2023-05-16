n=input()
l=[]
for i in n:
    if i>='0' and i<='9':
        l.append(i)
l1=list(map(int,l))
print(sum(l1))
