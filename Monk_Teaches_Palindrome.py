t=int(input())
for i in range(t):
    s=input()
    s2=s[::-1]
    if s!=s2:
        print("NO")
    elif s==s2 and len(s)%2==0:
        print("YES EVEN")
    else:
        print("YES ODD")