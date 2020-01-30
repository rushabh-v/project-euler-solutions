a={}
for i in range(1,100001):
    k=i
    if (str(i))[::]==(str(i))[::-1]:
        a[k]=i
                    
    else:
        for j in range(60):
            i+=int((str(i)[::-1]))
            if str(i)[::]==str(i)[::-1]:
                a[k]=i
                break
counts={}                   
n=input()
ma=0
k=0
for i in range(1,n+1):
    if i in a and a[i] in counts:
        counts[a[i]]+=1
    else:
        if i in a:
            counts[a[i]]=1
for i in counts:
    if counts[i]>ma:
        ma=counts[i]
        k=i
print k,ma
