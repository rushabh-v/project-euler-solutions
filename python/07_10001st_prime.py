primes=[True for i in range(1000000)]
primes[0]=False
primes[1]=False
for i in range(2,len(primes)-1):
    if primes[i]==True:
        j=i
        while j<=(len(primes)-1):
            j+=i
            if j<=(len(primes)-1):
                primes[j]=False
            else:
                break
                
o_p=[]
for i in range(len(primes)-1):
    if primes[i]==True:
        o_p.append(i)
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print o_p[n-1]
        
