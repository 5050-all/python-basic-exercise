import calendar
while True:
    try:
        y,m,x=map(int,input().split())
        total=0
        _,day_cnt=calendar.monthrange(y,m)
        target=str(x)
        for d in range(1,day_cnt+1):
            s=f"{y}-{m:02d}-{d:02d}"
            total+=s.count(target)
        print(total)
    except EOFError:
        break
            
            
        