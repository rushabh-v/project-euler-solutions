numbers={'1':'One','0':'\0'    ,'2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}

def fun(n):
    if n=='0':
        return ""
    elif len(n)==3 and n[0]=='0'and n[1]=='0' and n[2]=='0':
        return ""
    elif len(n)==3 and n[0]=='0' and n[1]=='0' and n[2]!='0':
        return numbers[n[2]]
    elif len(n)==3 and n[1]=='0' and n[2]=='0' and n[0]!='0':
        return numbers[n[0]]+' Hundred'
    elif len(n)==3 and n[0]!='0' and n[1]!='0' and n[2]=='0':
        return numbers[n[0]]+' Hundred '+numbers[str(int(n[1])*10)]
    elif len(n)==3 and n[0]!='0' and n[1]=='0' and n[2]!='0':
        return numbers[n[0]]+' Hundred '+numbers[n[2]]
    elif len(n)==3 and n[0]=='0' and n[1]!='0' and n[2]!='0':
        if (int(n[1])*10+int(n[2]))<=20:
            return numbers[str(int(n[1])*10+int(n[2]))]
        else:
            return numbers[str(int(n[1])*10)]+" "+numbers[n[2]]
    elif len(n)==3 and n[0]!='0' and n[1]!='0' and n[2]!='0' and (int(n[1])*10+int(n[2]))<20:
        return numbers[n[0]]+ " Hundred "+ numbers[str(int(n[1])*10+int(n[2]))]
    elif len(n)==3 and n[0]!='0' and n[1]!='0' and n[2]!='0' and int(n[1])*10+int(n[2])>=20:
        return numbers[n[0]]+" Hundred "+ numbers[str(int(n[1])*10)]+" "+numbers[n[2]]
    elif len(n)==2 and n[0]=='0' and n[1]=='0':
        return ""
    elif len(n)==2 and n[0]=='0' and n[1]!='0':
        return numbers[n[1]]
    elif len(n)==2 and n[0]!='0' and n[1]!='0':
        if int(n)<=20:
            return numbers[n]
        else:
            return numbers[str(int(n[0])*10)]+" "+numbers[n[1]]
    elif len(n)==2 and n[0]!='0' and n[1]=='0':
        return numbers[str(int(n[0])*10)]
    elif len(n)==1:
        return numbers[n]
    elif len(n)==1 and n[0]=='0':
        return ""
    
    
    
tests=int(raw_input())
for i in range(tests):
    n=raw_input()
    if int(n)==0:
        print "Zero"
        continue
    a=[]
    b=[]
    for i in range(len(n)):
        a.append(n[i])
    sum=0
    k=1
    count=0
    
    for j in range(len(a)):
        sum+=int(a[len(a)-j-1])*k
        k*=10
        count+=1
        if sum>=100 or count==3 or j==len(a)-1:
            b.append(str(sum))
            sum=0
            count=0
            k=1
    if len(b)==4 and fun(b[3])=='' and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])=='': 
        print fun(b[3]), fun(b[2]), fun(b[1]), fun(b[0])
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])=='': 
        print fun(b[3]), 'Billion'
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])!='': 
        print fun(b[3]), 'Billion', fun(b[0])
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])!='' and fun(b[1])=='' and fun(b[0])=='': 
        print fun(b[3]), 'Billion', fun(b[2]), 'Million'
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])=='' and fun(b[1])!='' and fun(b[0])=='': 
        print fun(b[3]), 'Billion', fun(b[1]), "Thousand"
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])=='' and fun(b[1])!='' and fun(b[0])!='': 
        print fun(b[3]), 'Billion', fun(b[1]), "Thousand", fun(b[0])
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])!='' and fun(b[1])!='' and  fun(b[0])=='': 
        print fun(b[3]), 'Billion', fun(b[2]), 'Million', fun(b[1]), 'Thousand'
    elif len(b)==4 and fun(b[3])=='' and fun(b[2])!='' and fun(b[1])=='' and  fun(b[0])!='': 
        print fun(b[2]), 'Million', fun(b[0])
    elif len(b)==4 and fun(b[3])=='' and fun(b[2])!='' and fun(b[1])=='' and fun(b[0])=='': 
        print fun(b[2]), 'Million'
    elif len(b)==4 and fun(b[3])=='' and fun(b[2])!='' and fun(b[1])!='' and fun(b[0])=='': 
        print fun(b[2]), 'Million', fun(b[1]), 'Thousand'
    elif len(b)==4 and fun(b[3])=='' and fun(b[2])=='' and fun(b[1])!='' and fun(b[0])=='': 
        print fun(b[1]), 'Thousand'
    elif len(b)==4 and fun(b[3])=='' and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])!='': 
        print fun(b[0])
    elif len(b)==4 and fun(b[3])!='' and fun(b[2])!='' and fun(b[1])!='' and fun(b[0])!='': 
        print fun(b[3]), "Billion", fun(b[2]), "Million", fun(b[1]), "Thousand", fun(b[0])
            
    elif len(b)==3 and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])=='':
        print fun(b[2]), fun(b[1]), fun(b[0])
    elif len(b)==3 and fun(b[2])!='' and fun(b[1])=='' and fun(b[0])=='':
        print fun(b[2]), 'Million'
    elif len(b)==3 and fun(b[2])!='' and fun(b[1])=='' and fun(b[0])!='':
        print fun(b[2]), 'Million', fun(b[0])
    elif len(b)==3 and fun(b[2])!='' and fun(b[1])!='' and fun(b[0])=='':
        print fun(b[2]), 'Million', fun(b[1]), 'Thousand'
    elif len(b)==3 and fun(b[2])=='' and fun(b[1])!='' and fun(b[0])=='':
        print fun(b[1]), 'Thousand'
    elif len(b)==3 and fun(b[2])=='' and fun(b[1])!='' and fun(b[0])!='':
        print fun(b[1]), 'Thousand', fun(b[0])
    elif len(b)==3 and fun(b[2])=='' and fun(b[1])=='' and fun(b[0])!='':
        print fun(b[0])
    elif len(b)==3 and fun(b[2])!='' and fun(b[1])!='' and fun(b[0])!='':
        print fun(b[2]), "Million", fun(b[1]), "Thousand", fun(b[0])
    
    elif len(b)==2 and fun(b[1])=='' and fun(b[0])=='': 
        print fun(b[1]), fun(b[0])
    elif len(b)==2 and fun(b[1])!='' and fun(b[0])=='':
        print fun(b[1]), 'Thousand'
    elif len(b)==2 and fun(b[1])!='' and fun(b[0])!='': 
        print fun(b[1]), 'Thousand', fun(b[0])
    elif len(b)==2 and fun(b[1])=='' and fun(b[0])!='': 
        print fun(b[0])
    elif len(b)==2 and fun(b[1])!='' and fun(b[0])!='': 
        print fun(b[1]), "Thousand", fun(b[0])
    
    elif len(b)==1:
        print fun(b[0])
