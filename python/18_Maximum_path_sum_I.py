def grtst_sum(pir,i,j):
    if i==len(pir)-2:
        if pir[i][j]+pir[i+1][j]>pir[i][j]+pir[i+1][j+1]:
            return pir[i][j]+pir[i+1][j]
        else:
            return pir[i][j]+pir[i+1][j+1]
    else:
        m=grtst_sum(pir,i+1,j)
        n=grtst_sum(pir,i+1,j+1)
        if m>n:
            return pir[i][j]+m
        else:
            return pir[i][j]+n
    
tests=input()
for i in range(tests):
    pir=[]
    n=input()
    for i in range(n):
        t=map(int,raw_input().strip().split())
        pir.append(t)
    if n==1:
        print pir[0][0]
    else:
        print grtst_sum(pir,0,0)
