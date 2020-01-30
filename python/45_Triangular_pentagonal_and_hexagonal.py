# python 2

from math import pow
[n, a, b]=map(int,raw_input().strip().split(' '))
[n, a, b]=[int(n), int(a), int(b)]
if a==3 and b==5:
    if n>10**14:
        n=10**14
    i=1
    while True:
        P=i*(3*i-1)/2
        if P>=n:
            break
        T=(pow(1+8*P,0.5)-1)/float(2)
        if T==round(T):
            print P
        i+=1
        if i>=n:
            break
if a==5 and b==6:
    i=1
    if n>10**14:
        n=10**14
    while True:
        P=i*(2*i-1)
        if P>=n:
            break
        T=(pow(1+24*P,0.5)+1)/float(6)
        if T==round(T):
            print P
        i+=1
        
