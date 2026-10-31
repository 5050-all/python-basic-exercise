T = int(input())
# 映射表
mp = {"zero":"0", "two":"2", "four":"4", "six":"6", "nine":"9"}
keys = ["zero","two","four","six","nine"]

for _ in range(T):
    s = input().strip()
    res = []
    i = 0
    n = len(s)
    while i < n:
        # 先判断是不是数字 0,2,4,6,9
        if s[i] in {'0','2','4','6','9'}:
            res.append(s[i])
            i += 1
        else:
            flag = False
            # 尝试匹配5个单词
            for word in keys:
                wlen = len(word)
                if i + wlen <= n and s[i:i+wlen] == word:
                    res.append(mp[word])
                    i += wlen
                    flag = True
                    break
            if not flag:
                i += 1
    print(''.join(res))
