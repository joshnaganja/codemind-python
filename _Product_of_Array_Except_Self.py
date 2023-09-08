n=int(input())
l=list(map(int,input().split()))
for i in l:
    a=1
    for j in l:
        if j==i:
            pass
        else:
            a=a*j
    print(a,end=" ")