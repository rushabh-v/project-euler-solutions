from math import pow
from math import sqrt
def is_pal(n):
    k=n
    count=0
    while k!=0:
        k=k/10
        count+=1
    sum=0
    a=n
    b=count-1
    while a!=0:
        sum+=(a%10)*pow(10,b)
        b-=1
        a=a/10
    if sum==n:
        return is_div(sum)
    else:
        return 0
def is_div(n):
    for i in range(100,int(sqrt(n)+1)):
        if n%i==0 and n/i>=100 and n/i<=999:
            return 1
    else:
        return 0

    
tests=int(raw_input())
for i in range(tests):
    var=int(raw_input())
    for j in range(1,1000000):
        b=var-j
        if is_pal(b)==1:
            print b
            break
