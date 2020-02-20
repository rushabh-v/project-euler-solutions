a=[0,0]
maxlen=0
maxnum=1
memo={}
for i in range(2,5000000):
    s=i
    l=0
    while s!=1:
        if s%2==0:
            s=s/2
            l+=1
            if s in memo:
                l+=memo[s]
                break
        else:
            s=3*s+1
            l+=1
    memo[i]=l
    if l<maxlen:
        a.append(a[i-1])
    else:
        maxlen=l
        maxnum=i
        a.append(maxnum)
           
t=input()
for i in range(t):
    n=input()
    print a[n]
    
            
