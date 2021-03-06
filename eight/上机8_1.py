import matplotlib.pyplot as plt
import numpy as np

fr = open("上机8.csv","r")
GDP_list = []
Year_list = []
New_Year_list = []
Label_list = []
Data_list = []

for line in fr:
    line = line.replace("\n", "")
    GDP_list.append(line.split(","))
fr.close()


for i in range(1,len(GDP_list[0])):
    Year_list.append(GDP_list[0][i])
Year_list.reverse()


for i in range(1,len(GDP_list)):
    Label_list.append(GDP_list[i][0])


for i in range(1,len(GDP_list)):
    ls = []
    for j in range(len(Year_list)):
        ls.append(eval(GDP_list[i][j+1]))
    ls.reverse()
    Data_list.append(ls)
for i in Year_list:
    c = i + '           '
    New_Year_list.append(c)
x = np.arange(0,6)
width = 0.1125
fig = plt.subplot()
rects0 = fig.bar(x - (15/2)*width, Data_list[0], width, color="coral", edgecolor="white", label=Label_list[0])
rects1 = fig.bar(x - (12/2)*width, Data_list[1], width, color="lightskyblue", edgecolor="white", label=Label_list[1])
rects2 = fig.bar(x - (9/2)*width, Data_list[2], width, color="violet", edgecolor="white", label=Label_list[2])
rects3 = fig.bar(x - (6/2)*width, Data_list[3], width, color="limegreen", edgecolor="white", label=Label_list[3])
rects4 = fig.bar(x - (3/2)*width, Data_list[4], width, color="dodgerblue", edgecolor="white", label=Label_list[4])
fig.set_xticks(x)
fig.set_xticklabels(New_Year_list)
fig.legend(loc = "best")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.grid(True)
plt.savefig("123.JPG") 
plt.show()

