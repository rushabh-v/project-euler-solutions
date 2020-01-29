from math import sqrt
def pan(n):
    return n*((3*n)-1)/2
n,k=map(int,raw_input().strip().split(" "))
[n,k]=[int(n),int(k)]
i=k+1
while True:
    a1=pan(i)+pan(i-k)
    a2=pan(i)-pan(i-k)
    a1=(sqrt((a1*24)+1)+1)/float(6)
    a2=(sqrt((a2*24)+1)+1)/float(6)
    if a1==round(a1) or a2==round(a2):
        print pan(i)
    i+=1
    if i>=n:
        break
