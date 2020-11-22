import random
ran=random.randint(1,100)
x=-1
while(x!=ran):
    x=int(input())
    if (x<ran):
        print("猜小了")
    if (x>ran):
        print("猜大了")
    if (x==ran):
        print("猜对了")
        break

