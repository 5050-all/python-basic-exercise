T = int(input())
for i in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    a=max(nums)
    b=min(nums)
    极差=a-b
    c=sum(nums)
    avg=c/len(nums)
    d=0
    for x in nums:
        d+=((x-avg)**2)
    方差=d / len(nums)
    print(f"{极差} {方差:.3f}")