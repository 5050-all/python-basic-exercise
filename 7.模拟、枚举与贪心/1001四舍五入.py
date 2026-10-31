n, t = map(int, input().split())
s = list(input().strip())

while t > 0 and '.' in s:
    dot = s.index('.')
    i = dot + 1
    find_pos = -1
    while i < len(s):
        if int(s[i]) >= 5:
            find_pos = i
            break
        i += 1
    if find_pos == -1:
        break
    t -= 1
    s = s[:find_pos]
    carry = 1
    j = find_pos - 1
    while carry and j >= 0:
        if s[j] == '.':
            j -= 1
            continue
        val = int(s[j]) + carry
        if val == 10:
            s[j] = '0'
            carry = 1
        else:
            s[j] = str(val)
            carry = 0
        j -= 1
    if carry:
        s.insert(0, '1')

res = ''.join(s).rstrip('0').rstrip('.')
print(res)