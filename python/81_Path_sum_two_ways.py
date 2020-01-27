# python 2

import sys
sys.setrecursionlimit(10000) 
memo={}
matrix=[]
def findsum(i,j,n):
    #print i,j,n,"|||"
    if i==n-1 and j==n-1:
        return matrix[i][j]
    elif i==n-1:
        s=0
        while j<=n-1:
            s+=matrix[i][j]
            j+=1
        return s
    elif j==n-1:
        s=0
        while i<=n-1:
            s+=matrix[i][j]
            i+=1
        return s
    else:    
        if (i,j+1) in memo:
            #print i,j+1,n,";;;;"
            a=memo[(i,j+1)]
        else:
            a=findsum(i,j+1,n)
        if (i+1,j) in memo:
            b=memo[(i+1,j)]
        else:
            b=findsum(i+1,j,n)
        if a>b:
            memo[(i,j)]=matrix[i][j]+b
            return matrix[i][j]+b
        else:
            memo[(i,j)]=matrix[i][j]+a
            return matrix[i][j]+a


n=input()
for i in range(n):
    matrix.append(map(int,raw_input().strip().split(' ')))
#matrix=[[i for i in range(1,502)] for j in range(501)]
print findsum(0,0,n)
