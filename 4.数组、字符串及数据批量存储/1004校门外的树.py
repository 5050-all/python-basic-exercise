L,M=map(int,input().split())
tree = [True] * (L + 1)

for _ in range(M):
    l, r = map(int, input().split())
    # 区间[l, r]的树移走，标记为False
    for i in range(l, r + 1):
        tree[i] = False

# 统计剩下为True的数量
res = sum(tree)
print(res)