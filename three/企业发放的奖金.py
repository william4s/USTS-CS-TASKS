a=float(input())
ans=0
if (a<=10):
    ans=a*0.1
elif (10<a<=20):
    ans=10*0.1+(a-10)*0.075
elif(20<a<=40):
    ans=10*0.1+10*0.075+(a-20)*0.05
elif(40<a<=60):
    ans=10*0.1+10*0.075+20*0.05+(a-40)*0.03
elif (60<a<=100):
    ans=10*0.1+10*0.075+20*0.05+(60-40)*0.03+(a-60)*0.015
elif (a>100):
    ans=10*0.1+10*0.075+20*0.05+(60-40)*0.03+(100-60)*0.015+(a-100)*0.01
print(ans)
