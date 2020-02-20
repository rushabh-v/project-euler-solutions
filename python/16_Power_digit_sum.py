
tests=int(raw_input())
for i in range(tests):
    n=int(raw_input())
    k=2**n
    sum=0
    while k!=0:
        sum+=k%10
        k=k/10
    print sum
