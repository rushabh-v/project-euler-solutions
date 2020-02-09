#!/bin/python
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n==1:
        print int('1')
    else:
        i=n*(n-1)
        l=n-2
        while True:
            for j in range(2,n):
                if i%j!=0:
                    k=0
                    i+=n
                    
                    break
                else:
                    k=1
            if k==1:
                print i
                break
        
    
