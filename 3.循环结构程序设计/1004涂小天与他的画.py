T = int(input())
for _ in range(T):
    n = int(input())
    mid = n // 2
    # 打印上半部分（含中间一行）
    for i in range(mid + 1):
        stars = 2 * i + 1
        blank = mid - i
        print(" " * blank + "*" * stars)
    # 打印下半部分
    for i in range(mid - 1, -1, -1):
        stars = 2 * i + 1
        blank = mid - i
        print(" " * blank + "*" * stars)
