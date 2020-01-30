from itertools import permutations
def gvsm(n):
    s=0
    for i in range(len(n)):
        s+=int(n[i])*(10**(len(n)-i-1))    
    return s
n=input()
su=[]
k=n/2
l=[i for i in range(1,n+1)]
per2=list(permutations(l,k))
for i in per2:
    e=[h for h in range(1,n+1)]
    for j in range(len(i)):
        e.remove(i[j])
    per1=list(permutations(e))
    for c in (per1):
        if gvsm(c[:len(c)/2+1])*gvsm(c[len(c)/2+1:len(c)])==gvsm(i)
              or gvsm(c[:len(c)/2])*gvsm(c[len(c)/2:len(c)])==gvsm(i)
              or gvsm(c[:len(c)/2-1])*gvsm(c[len(c)/2-1:len(c)])==gvsm(i):
            su.append(gvsm(i))       
su=sorted(su)
su=list(set(su))
s=0       
for i in range(len(su)):
    s+=su[i]
print s
    
