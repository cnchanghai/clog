#coding:utf-8
from bs4 import BeautifulSoup
import requests
import re


def mtbinfo():
    dlist=[]
    url='http://www.moko.cc/mtb.html'
    r=requests.get(url, verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    modlist=soup.find_all('div','sub_show')
    link=[]
    for i in modlist:
        if i==modlist[-1] or i==modlist[0]:
            continue
        tmp=i.find_all('a')
        for j in tmp:
            if '?' in j['href']:
                pass
            else:
                dic=[]
                dic.append(j['href'].split('/')[-2])
                url2='http://www.moko.cc/mtb/model/'+dic[0]+'/space.html'
                r2=requests.get(url2, verify=False)
                content2=r2.content
                soup2=BeautifulSoup(content2,'lxml')
                uname=soup2.find(name='div',attrs={"class":"username"}).text
                dic.append(uname)
                blist=soup2.find_all(name='input',attrs={"name":re.compile(r'modelBean.*')})
                for item in blist:
                    dic.append(item.get('value'))
            dlist.append(dic)
    return dlist
def mtbtu(uid):
    url='http://www.moko.cc/mtb/model/'+uid+'/space.html'
    piclist=[]
    r=requests.get(url, verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    blist=soup.find_all('dd')
    for item in blist:
        link2=item.find('img')
        try:
            if '.png' in link2['src']:
                pass   
            else:
                piclist.append(link2['src'].split('?')[0])
        except:
            continue

    return piclist
if __name__=='__main__':
    #dlist=mtbinfo()
    #print len(dlist)
    piclist= mtbtu('31959')
    print(piclist)
  
