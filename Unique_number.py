n=int(input())
s=str(n)
l1=[]
for i in s:
    if i not in l1:
        l1.append(i)
    else:
        pass
if len(s)==len(l1):
    print("Unique Number")
else:
    print("Not Unique Number")