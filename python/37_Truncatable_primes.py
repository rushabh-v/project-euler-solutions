pr=[True for i in range(1000001)]
pr[0]=False
pr[1]=False
for i in range(2,1000001):
    if pr[i]==True:
        j=i
        while j<=1000000:
            j+=i
            if j>1000000:
                break
            pr[j]=False
primes=[]
for i in range(10,1000001):
    if pr[i]==True:
        a=str(i)
        for j in range(len(a)-1):
            if pr[int(a[:len(a)-j-1])]==False or pr[int(a[j+1:])]==False:
                break
        else:
            primes.append(i)
n=input()
s=0
for i in primes:
    if i<n:
        s+=i
    else:
        break
print s
