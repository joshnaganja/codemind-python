s=input()
c=0
for i in range(1,len(s)-1):
    if s[i].isupper():
        c=c+1
print(c+1)