sms=[]
sums=[0,0]
primes=[True for i in range(1000001)]
primes[0]=False
primes[1]=False
s=0
for i in range(2,len(primes)-1):
    if primes[i]==True:
        s+=i
        sms.append(s)
        j=i
        while j<=(len(primes)-1):
            j+=i
            if j<=(len(primes)-1):
                primes[j]=False
            else:
                break
    sums.append(sms[len(sms)-1])
                
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sums[n]
    
