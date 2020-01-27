# python 2

def countsum(T,i,j,n):
    if n==1:
        return T[0][0]
    if i==n-2:
        if (i,j) in memo:
            return memo[(i,j)]
        if T[i+1][j]>T[i+1][j+1]:
            memo[(i,j)]=T[i][j]+T[i+1][j]
            return T[i][j]+T[i+1][j]
        else:
            memo[(i,j)]=T[i][j]+T[i+1][j+1]
            return T[i][j]+T[i+1][j+1]
    if (i+1,j) in memo:
        a=memo[(i+1,j)]
    else:
        a=countsum(T,i+1,j,n)
    if (i+1,j+1) in memo:
        b=memo[(i+1,j+1)]
    else:
        b=countsum(T,i+1,j+1,n)
    if a>b:
        memo[(i,j)]=T[i][j]+a
        return T[i][j]+a
    else:
        memo[(i,j)]=T[i][j]+b
        return T[i][j]+b

for i in range(input()):
    T=[]
    memo={}
    n=input()
    for j in range(n):
        T.append(map(int,raw_input().strip().split(' ')))
    print countsum(T,0,0,n)
        
     
    
