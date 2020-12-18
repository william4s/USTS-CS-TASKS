import matplotlib.pyplot as plt
fr = open("上机8.csv","r")
GDP_list = []
Year_list = []
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
        ls.sort()
    Data_list.append(ls)

ax = plt.subplot()
color_list = ["coral", "lightskyblue", "violet", "limegreen", "dodgerblue", "red"]
plt.pie(x= Data_list[0], labels= Year_list, colors= color_list)
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.show()
