year,month,day=map(int,input().split())
if ((year%4==0 and year%100!=0)or(year%400==0 and year%4000!=0)):
    pd=1
else:
    pd=0
m=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,12):
    m[i]=m[i-1]+m[i]
ans=0
if (pd):
    if (month>2):
        ans=m[month-1]+day+1
    else:
        ans=m[month-1]+day
else:
    ans=m[month-1]+day
print(ans)