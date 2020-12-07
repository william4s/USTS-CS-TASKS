import math
def isprime(x):
    t=int(math.sqrt(x))
    for i in range(2,t+1):
        if (x%i==0):
            return 0
    return x
for i in range(3,10001):
    for j in range(2,int(math.sqrt(i))):
        if (i==isprime(j)+isprime(i-j)):
            print("i:{}= {} + {} ".format(i,j,i-j))
            break