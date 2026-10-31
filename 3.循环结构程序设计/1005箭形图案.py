while True:
    try:
        n=int(input())
        for i in range(1,n+2):
            stars = i 
            blank = 2 * (n+1-i)
            print(" " * blank + "*" * stars)
        for i in range(n,0,-1):
            stars = i 
            blank = 2 * (n+1-i)
            print(" " * blank + "*" * stars)
    except EOFError:
        break
    