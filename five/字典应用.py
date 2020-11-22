#stu={"001":["william4s","NUS"],"002":["John","NJUPT"],"003":["ZZ","NJU"],"004":["NSZ","PKU"]}
stu={"ID":"19200124214","Name":"william4s","University":"NUS"}
stu["Grade"]=10
print(stu.items())
print(stu.keys())
print(stu.values())
del stu["University"]
print(stu.items())