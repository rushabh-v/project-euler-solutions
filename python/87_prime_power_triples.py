IsPrime=[True for i in range (3164)]
primes=[]
IsPrime[0]=False
IsPrime[1]=False
for i in range(len(IsPrime)):
    if IsPrime[i]==True:
        primes.append(i)
        m=i+i
        while m<3164:
            IsPrime[m]=False
            m+=i

sprimes=[]
for i in primes:
    for j in primes:
        for k in primes:
            s=pow(i,4)+pow(j,3)+pow(k,2)
            if s>10000000-1:
                break
            sprimes.append(s)
            #print(i,j,k,s)

sprimes=sorted(set(sprimes))
ns=[0 for i in range(10000000)]
a=0
n=0
for i in range(len(ns)):
    if sprimes[a]<=i:
        a+=1
        n+=1
        if a>=len(sprimes)-1:
            rem=i
            rem2=n
            break            
    ns[i]=n

for _ in range(int(input())):
    a=int(input())
    if a>=rem:
        print(rem2)
    else:
        print(ns[a])
