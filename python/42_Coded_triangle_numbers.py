from math import sqrt
t=input()
for i in range(t):
    n=input()
    a=((sqrt(8*n+1)-1)/2)
    b=round(a)
    if b==a:
        print int(a)
    else:
        print -1
