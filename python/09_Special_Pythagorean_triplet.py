t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    max=1
    for j in range(2,n/2):
        a=j
        b=((n*n)-2*n*a)/(2*n-2*a)
        c=n-a-b
        mult=a*b*c
        if mult>max and (c*c)==(b*b)+(a*a):
            max=mult
    if max==1:
        max=-1
    print max
    
    
        
            
