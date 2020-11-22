ls = [int(x) for x in input().split()]
l=len(ls)
#print(l)
x=int(input())
pd=int(1)
if x<ls[0]:
    ls.insert(0,x)
    pd=0
for i in range(0,l-1):
    if (x>=ls[i] and x<ls[i+1] and pd):
        ls.insert(i+1,x)
        pd=0
        break
if pd==1 :
    ls.append(x)
print(ls)