n=input()
a=1
b=1
a1=1
b1=1
for i in range(n):
    a=a1+b1+b1
    b=a1+b1
    if len(str(a))>len(str(b)):
        print i+1
    a1=a
    b1=b
