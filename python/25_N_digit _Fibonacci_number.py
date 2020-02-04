dic={}
i=2
count=0
a=1
count+=1
b=1
count+=1
while i<=5000:
    c=a+b
    count+=1
    if len(str(c))==i:
        dic[i]=count
        i+=1   
    b=c+a
    count+=1
    if len(str(b))==i:
        dic[i]=count
        i+=1    
    a=b+c
    count+=1
    if len(str(a))==i:
        dic[i]=count
        i+=1
t=input()
for i in range(t):
    n=input()
    print dic[n]
