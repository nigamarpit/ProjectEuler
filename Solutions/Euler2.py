def Euler2():
    d = dict()
    d[1]=1
    d[2]=2
    x = 3
    n=0
    s=2    
    while(n < 4000000):
        n=d[x-1]+d[x-2]
        d[x]=n
        x+=1
        if n%2==0:
            s+=n
    return s

print(Euler2())