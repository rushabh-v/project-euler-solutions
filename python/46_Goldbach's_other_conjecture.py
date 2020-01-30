from math import pow
prs=[]
primes=[True for i in range(500000)]
primes[0]=False
primes[1]=False
for i in range(2,len(primes)-1):
    if primes[i]==True:
        prs.append(i)
        j=i
        while j<=(len(primes)-1):
            j+=i
            if j<=(len(primes)-1):
                primes[j]=False
            else:
                break
for i in range(input()):
    n=input()
    count=0
    for j in prs:
        if j>n:
            print count
            break
        T=pow((n-j)/float(2),0.5)
        if T==round(T):
            count+=1
            
        
