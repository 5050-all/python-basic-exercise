n,k=map(int,input().split())
Ai=list(map(int,input().split()))
Bi=list(map(int,input().split()))
sumB=sum(Bi)
diff=[Ai[i]-Bi[i] for i in range(n)]
diff.sort(reverse=True)

ans=sumB+sum(diff[:k])
print(ans)