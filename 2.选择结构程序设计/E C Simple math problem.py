X,Y=map(int,input().split())
if Y % X ==0:
    Z=X + Y
    print(Z)
else:
    Z = Y-X
    print(Z)