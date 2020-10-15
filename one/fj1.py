#william4s
#附加题：编程计算1+(1+2)+(1+2+3)+……+(1+2+3+……+10)的值。
a,ans=0,0
for i in range(0,10):
    a+=i
    ans+=a
print(ans)