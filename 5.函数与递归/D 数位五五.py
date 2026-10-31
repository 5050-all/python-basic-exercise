x,y=map(int,input().split())
cnt=0
for i in range (x,y+1):
    s=0
    for c in str(i):
        s+=int(c)
    if s%5==0:
        cnt+=1
print(cnt)