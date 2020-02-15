from math import factorial as fact
tests=int(raw_input())
for i in range(tests):
    m, n=raw_input().split()
    [m,n]=[int(m),int(n)]
    print (((fact(m+n))/(fact(m)*fact(n)))%1000000007)
    

        

    
