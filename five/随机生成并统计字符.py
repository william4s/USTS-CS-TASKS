import random
lt=[]
for i in range(0,130):
    lt.append(0)
for i in range(0,1000):
    t=random.randint(0,127)
    lt[t]+=1
for i in range(0,128):
    print("{} {}".format(chr(i),lt[i]))
