ans = []
#第一种：1位数 * 4位数 = 4位数
for a in range(1,10):
    for b in range(1000,10000):
        c = a * b
        s = str(a) + str(b) + str(c)
        if len(s) != 9:
            continue
        if set(s) =={'1','2','3','4','5','6','7','8','9'}:
            small = min(a,b)
            big = max(a,b)
            ans.append((c,small,big))
#第二种：2位数 * 3位数 = 4位数
for a in range(10,100):
    for b in range(100,1000):
        c = a * b
        s = str(a) + str(b) + str(c)
        if len(s) != 9:
            continue
        if set(s) =={'1','2','3','4','5','6','7','8','9'}:
            small = min(a,b)
            big = max(a,b)
            ans.append((c,small,big))
 
#去重
res = []
for item in ans:
    if item not in res:
        res.append(item)
res.sort(key = lambda x:(x[0],x[1]))
 
for c,a,b in res:
    print(f"{c} = {a} x {b}")
