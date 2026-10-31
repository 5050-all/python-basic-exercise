c = list(map(int, input().split()))
total = sum(c)
 
if total == 0:
    print(-1)
elif total == 1:
    print(next(d for d in range(10) if c[d]))
elif sum(1 for d in range(10) if c[d] % 2) > 1:
    print(-1)
else:
    half = [c[d] // 2 for d in range(10)]
    mid = next((str(d) for d in range(10) if c[d] % 2), "")
 
    first = -1
    for d in range(1, 10):         
        if half[d]:
            first = d
            break
    if first == -1:
        print(-1)
    else:
        half[first] -= 1
        left = str(first) + "".join(str(d) * half[d] for d in range(10))
        print(left + mid + left[::-1])