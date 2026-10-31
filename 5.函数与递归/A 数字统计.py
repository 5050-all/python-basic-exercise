L,R=map(int,input().split())
cnt=0
for i in range(L,R+1):
    s = str(i)
    cnt+=s.count('2')
print(cnt)