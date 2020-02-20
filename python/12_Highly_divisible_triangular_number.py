primes=[]
p=[True for i in range(100000)]
p[0]=False
p[1]=False
i=2
while i<=(len(p)-1):
    j=i
    primes.append(i)
    while j<=(len(p)-1):
        j+=i
        if j<=(len(p)-1):
            p[j]=False
        else:
            break
    i+=1
    while i<=(len(p)-1) and p[i]!=True:
        i+=1
div={0:[1,1],1:[3,2],2:[6,4],3:[6,4]}
j=4
i=4
while i<=1000:
    while True:
        sum=(j*(j+1))/2
        mult=1
        a=sum
        for k in primes:
            count=0
            while a%k==0:
                a=a/k
                count+=1
                if a==1 or a%k!=0:
                    break
            mult*=(count+1)
            count=0
            if a==1:
                j+=1
                break
        if mult>i:
            q=sum
            q1=mult
            for s in range(i,mult):
                div[s]=[q,q1]
            i=mult
            mult=1
            break

t=input()
for i in range(t):
    n=input()
    print div[n][0]
            
