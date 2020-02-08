tests=int(raw_input())
for i in range(tests):
    var=int(raw_input())
    sum=2
    a=1
    b=2
    c=0
    while a<var and b<var and c<var:
        c=a+b
        if c%2==0 and c<var:
            sum+=c
        a=b+c
        if a%2==0 and a<var:
            sum+=a
        b=a+c
        if b%2==0 and b<var:
            sum+=b
    print sum
