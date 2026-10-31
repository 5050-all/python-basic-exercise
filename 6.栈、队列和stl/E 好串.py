s=input().strip()
stk=[]
for c in s:
    stk.append(c)
    if len(stk)>=2 and stk[-2]=='a' and stk[-1]=='b':
        stk.pop()
        stk.pop()
if not stk:
    print("Good")
else:
    print("Bad")
    