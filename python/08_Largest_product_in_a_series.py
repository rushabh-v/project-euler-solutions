#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input()
    a=[]
    b=num
    l=len(b)
    for i in range(l):
        a.append(int(b[i]))
   
    max=0
    i=0
    for i in range(n-k-1):
        mult=1
        for j in range(k):
            mult=mult*a[i+j]
        if mult>max:
            max=mult
    print max        
    
