x=str(input())
pd=int(1)
if len(x)!=5 :
    print("INPUT ERROR!")
else:
    for i in range(0,2) :
        if x[i]!=x[5-i-1] :
            pd=0
if pd :
    print("YES")
else:
    print("NO")
