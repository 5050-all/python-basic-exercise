ch = input().strip()
n = ord(ch) - ord('A')
for i in range(n + 1):
    print(' ' * (n - i), end='')
    for j in range(i + 1):
        print(chr(ord('A') + j), end='')
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end='')
    print()
