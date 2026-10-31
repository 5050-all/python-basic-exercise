for j in range(1, 10):
    line = []
    for i in range(1, j + 1):
        res = i * j
        line.append(f"{i}*{j}={res:2d}")
    print(' '.join(line))
