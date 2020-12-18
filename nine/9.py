import requests
from bs4 import BeautifulSoup
import bs4
import matplotlib.pyplot as plt

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.157 Safari/537.36"}

ulist=[]
time=[]
price=[]
def getHTMLText(url):#获取URL信息，输出内容
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        r.encoding='utf-8'
        return r.text
    except:
        return""
def fillList(soup):
    ALL=soup.find_all('a','nostyle')
    for a in ALL:
        span=a.find('span')
        b=a.find('b')
        em=a.find('em')
        temp=[]
        temp.append([b.string,span.string,em.string])
        ulist.append(temp)

    
def printList(num):

    for i in range(num):
        time.append(ulist[i][0][0])
        price.append(int(ulist[i][0][1][0:-3]))

def main():
    url='http://139.196.44.142/fangjia/suzhou2020/'
    html=getHTMLText(url)
    soup=BeautifulSoup(html,'html.parser')
    fillList(soup)
    printList(len(ulist))
    l=len(time)
    for i in range(0,int(l/2)):
        time[i],time[l-i-1]=time[l-i-1],time[i]
    l=len(price)
    for i in range(0,int(l/2)):
        price[i],price[l-i-1]=price[l-i-1],price[i]
    #print(price)
    plt.plot(time,price,linewidth=1)
    plt.title("折线图",fontsize=20)
    plt.xlabel("横坐标",fontsize=14)
    plt.ylabel("纵坐标",fontsize=14)
    plt.tick_params(axis='both',labelsize=5)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()
main()