n = int(input())
a = []
b = [0]*(n)
for j in range(n):
    a.append(b[:])
s = n*n
t = 2
x , y = 0 , 0
a[x][y]=1
while t<=s :
    while(y+1<n and a[x][y+1]==0):
        a[x][y+1]=t
        #print("x: {} y:{} ".format(x,y))
        t+=1
        y+=1

    while(x+1<n and a[x+1][y]==0):
        a[x+1][y]=t
        #print("  x: {} y:{} ".format(x,y))
        t+=1
        x+=1
    while(y-1>=0 and a[x][y-1]==0):
        a[x][y-1]=t
        #print("x: {} y:{} ".format(x,y))
        t+=1
        y-=1
    while(x-1>=0 and a[x-1][y]==0):
        a[x-1][y]=t
        #print("x: {} y:{} ".format(x,y))
        t+=1
        x-=1
with open("file.out", "w") as file:
    for p in a:
        for f in p:
            file.write("%5d"%f)
        file.write("\n")
