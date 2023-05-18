n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=[]
for i in l:
    if i+n1>=max(l):
        print("True",end=' ')
    else:
        print("False",end=' ')