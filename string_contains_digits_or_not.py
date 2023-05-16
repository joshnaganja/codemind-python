n=int(input())
for i in range(n):
    n1=input()
    c=0
    for j in n1:
        if j>='0' and j<='9':
            c+=1
    if c!=0:
        print("Yes")
    else:
        print("No")
    