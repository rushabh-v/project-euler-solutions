tests=int(raw_input())

for i in range(tests):
    var=int(raw_input())
    sum=0
    if var%5==0 and var%3==0:
        sum=((var/3)*(var/3+1)/2)*3+((var/5)*(var/5+1)/2)*5 -var-((var/15)*(var/15+1)/2)*15
    elif var%5==0 and var%3!=0:
        sum=((var/3)*(var/3+1)/2)*3+((var/5)*(var/5+1)/2)*5-var-((var/15)*(var/15+1)/2)*15
    elif var%5!=0 and var%3==0:
        sum=((var/3)*(var/3+1)/2)*3+((var/5)*(var/5+1)/2)*5-var-((var/15)*(var/15+1)/2)*15
    elif var%5!=0 and var%3!=0:
        sum=((var/3)*(var/3+1)/2)*3+((var/5)*(var/5+1)/2)*5-((var/15)*(var/15+1)/2)*15
    print sum
