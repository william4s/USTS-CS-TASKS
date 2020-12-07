import math
t=int(0)
a=int(input())
b=int(input())
c=int(input())
def f1(a,b,c):
    return (-b+math.sqrt(t))/(2*a),(-b-math.sqrt(t))/(2*a)
def f2(a,b,c):
    return (-b+math.sqrt(t))/(2*a)
def f3(a,b,c):
    return "不存在根"
f=lambda a,b,c: b*b-4*a*c

t=f(a,b,c)
if (t>0):
    x1,x2=f1(a,b,c)
    print("x1={} x2={}".format(x1,x2))
elif (t==0):
    print(f2(a,b,c))
else:
    print(f3(a,b,c))
