for a in range(0,1000):
    sum=0
    for x in range(1,101):
        for y in range (1,101):
            if (3*x+y>48) or(x>y) or (4*x+y<a):
                sum+=1
    if sum ==10000:
        print(a)
