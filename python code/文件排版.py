fo=open("listin.txt","r")
ft=open("listout.txt","w")
n=int(input())
data = fo.readlines()
a=[]
for line in data:
    pd=True
    if (line=='\n'):
        continue
    le=len(line)
    for i in range(0,le):
        if (line[i]==' ' or line[i]=='\t'):
            if pd==False :
                a.append(" ")
                pd=True
            else:
                continue
        else:
            a.append(line[i])
            pd=False
    l=len(a)
    for i in range(0,l):
        if (a[i]==":"):
            if (a[i+1]!=' '):
                a.insert(i+1,' ')
            j=i+1
            while j<n:
                a.insert(j-1,' ')
                j+=1
            break;    
    str1="".join(a)
    ft.write(str1)
    a=[]
fo.close
#作者：william4s
#2020-12-7
#如果对你有帮助，不妨右上角star一下，感谢