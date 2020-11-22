days=365
ans=1.0
cnt=0
wk=0
while days!=0 :
    if cnt==0 :
        cnt+=1
        days-=1
        continue
    if wk%7==0 :
        wk=0
    if 3<=wk<=6 :
        ans*=1.01
    wk+=1
    if cnt%10==0 :
        wk=0
        cnt=0
    cnt+=1
    days-=1
print("{}".format(ans))