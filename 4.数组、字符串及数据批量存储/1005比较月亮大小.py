cycle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
         14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L = len(cycle)

n = int(input())
rec = list(map(int, input().split()))

candidates = []
for start in range(L):
    ok = True
    for i in range(n):
        pos = (start + i) % L
        if cycle[pos] != rec[i]:
            ok = False
            break
    if ok:
        end_idx = (start + n - 1) % L
        next_val = cycle[(end_idx + 1) % L]
        candidates.append(next_val)

last = rec[-1]
all_up = all(v > last for v in candidates)
all_down = all(v < last for v in candidates)

if all_up:
    print("UP")
elif all_down:
    print("DOWN")
else:
    print(-1)
