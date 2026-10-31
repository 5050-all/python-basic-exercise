import math
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3,sqrt_n+1,2):
        if n % i == 0:
            return False
    return True
s = input().strip()
pal_str = s + s[:-1][::-1]
pal_num = int(pal_str)
if is_prime(pal_num):
    print("prime")
else:
    print("noprime")
        