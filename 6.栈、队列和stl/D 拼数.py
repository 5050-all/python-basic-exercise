n = int(input())
s = input().split()
for i in range(n):
    for j in range(i+1, n):
        if s[i]+s[j] < s[j]+s[i]:
            s[i], s[j] = s[j], s[i]
print(''.join(s))