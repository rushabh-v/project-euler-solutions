n=int(raw_input())
sum=0
for i in range(n):
    var=int(raw_input())
    sum+=var
a=[]

while sum!=0:
    k=sum%10
    a.append(k)
    sum=sum/10
sum=0    
for i in range(0,10):
    sum+=a[len(a)-i-1]*10**(10-i-1)
print sum
    
