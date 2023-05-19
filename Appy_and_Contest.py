t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c=(n//a)+(n//b)
    if c>k:
        print("Win")
    else:
        print("Lose")