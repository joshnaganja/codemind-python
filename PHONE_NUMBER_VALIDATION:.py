n=int(input())
s=str(n)
if s.startswith('0') or len(s)>=11 or len(s)<10:
    print("Invalid")
else:
    print("Valid")