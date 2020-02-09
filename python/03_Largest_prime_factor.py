from math import sqrt
t=input()
for i in range(t):
    n=input()
    b=0
    while n%2==0:
        n=n/2
        if n==1:
            b=1
            print 2
            break
    if b==0:
        j=3
        while j<=int(sqrt(n)):
            if n%j==0:
                n=n/j
            else:
                j+=2
                
        if n>2:
            print n
        else:
            print j
