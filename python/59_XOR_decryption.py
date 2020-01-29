cw=[32,40,41,58,59,46,39,44,63,45,33,48, 49, 50, 51, 52,53, 54, 55, 56, 
    57,65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
    81, 82, 83, 84, 85, 86, 87, 88, 89,90,97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108,109, 110, 111, 112, 113, 114, 115,
    116, 117, 118, 119, 120,121, 122]


n=input()
a=map(int,raw_input().strip().split(' '))
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            var=1
            for c in range(len(a)):
                if c%3==0:
                    a1=a[c]^i
                elif c%3==1:
                    a1=a[c]^j
                elif c%3==2:
                    a1=a[c]^k
                if a1 not in cw:
                    break
            else:
                print chr(i)+chr(j)+chr(k)
                var=0
                break
            if var==0:
                break
        if var==0:
            break
    if var==0:
        break
                

