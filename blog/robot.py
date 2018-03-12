#coding=utf8
from bs4 import BeautifulSoup
import requests
import random
import time
import selenium.webdriver
import re
from datetime import datetime,timedelta
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def new163(link):
    news=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(20)
    driver.get(link)
    content=driver.page_source
    #print content
    soup=BeautifulSoup(content,'lxml')
    #print soup
    items=soup.find_all('div',attrs={'class',"data_row news_article clearfix"})
    for i in items:
        dic={}
        dic['title']=i.find('h3').text
        dic['link']=i.find('a')['href']
        dic['tag']=i.find('strong').text
        dic['img']=i.find('img')['src'].split('?')[0]
        t=i.find('span',attrs={'class':'time'}).text
        if u'小时' in t:t=datetime.now()-timedelta(hours=int(t.strip(u'小时前')))
        elif u'天' in t:t=datetime.now()-timedelta(days=int(t.strip(u'天前')))
        elif u'分钟' in t:t=datetime.now()-timedelta(minutes=int(t.strip(u'分钟前'.strip('-'))))
        dic['time']=t
        news.append(dic)
    return news

def qiushi(m):
    e='';
    qiushi_list=[]
    url = 'https://www.qiushibaike.com/hot/page/' + str(m)
    try:
        req= requests.get(url,verify=False)
        res= req.content
        soup=BeautifulSoup(res,"lxml")
        items=soup.findAll('div',"mb15")
        for item in items:
            qiushi_dic={}
            if item.find('div', 'thumb'):
                continue
            if item.find('div', 'video_holder'):
                continue
            author = item.find("h2")
            if author != None:
                author = author.get_text().strip()
            content = item.find("div", 'content').get_text().strip()
            qiushi_dic['a']=author
            qiushi_dic['c']=content
            qiushi_list.append(qiushi_dic)

    except Exception as e:
            if hasattr(e,"code"):
                pass
            if hasattr(e,"reason"):
                pass
    return qiushi_list
def getcontent(link):
    r=requests.get(link,verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    zhengwen=soup.find('div','body').text
    #print zhengwen+'\n first\n'
    zhengwen1=zhengwen.split('\n\n')[0].strip('\n \n')
    #zhengwen1=zhengwen.split('\n\n')[0].strip('\n \n')
    if zhengwen1=='':
        zhengwen1=zhengwen.split('\n\n')[1].strip('\n \n')
    zhengwen=zhengwen1
    #print zhengwen+'\n second\n'
    zhengwen=zhengwen.replace('\n','<br>') 
    return zhengwen
def lssdjt(m,d):
    url='http://www.todayonhistory.com/'+str(m)+'/'+str(d)+'/'
    print(url)
    lslist=[]
    r = requests.get(url, verify=False)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
    linklist = soup.find_all('li', 'circlel')
    for link in linklist:
        if link == linklist[0]:
            continue
        else:
            try:
                dic={}
                dic['year']=link.find('span', 'poh').text
                #print dic['year']
                dic['title']= link.find('a').get('title')
                #print dic['title']
                lislink = link.find('a').get('href')
                dic['content']=getcontent(lislink)
                #dic['m']=m
                #dic['d']=d
                if dic['content']=='':continue
            except:
                continue
        lslist.append(dic)
    return lslist
def zimeiti(page):
    meiti_list=[]
    url = 'http://pinyin.sogou.com/zimeiti/index/'+str(page)
    req= requests.get(url,verify=False)
    res= req.content
    soup=BeautifulSoup(res,"lxml")
    items=soup.findAll('li',attrs={'id':re.compile(r'^\d+')})
    for item in items:
        dic={}
        dic['zid']=item['id']
        dic['des']=item.find('p').text.strip()
        dic['title']=item.find('h4').text
        dic['tag']=item.find('i').text
        dic['img']=item.find('img')['src']
        dic['url']=item.find('a')['href']
        tmp=item.find('span').text.split()
        dic['author']=tmp[0]
        dic['date']=tmp[-1]
        meiti_list.append(dic)
    return meiti_list
def yaoyans(cata,page):
    list=[]
    urln='.'
    if page>0:urln='_'+str(page)+'.'
    url='http://py.zjol.com.cn/'+cata+'/index'+urln+'shtml'
    print(url)
    r = requests.get(url,verify=False)
    soup = BeautifulSoup(r.content,"lxml")
    ylist=soup.find_all('li',attrs={'class':"listLi"})
    for item in ylist:
        dic={}
        dic['date']=datetime.strptime(item.find('span').text,'%Y年%m月%d日%H时')
        dic['url']=item.find('a')['href']
        dic['title']=item.find('a').text
        list.append(dic)
    return list
def shicicontent(link):
    #link='http://www.qinqishuhua.org/show-215-62653-1.html'
    #link='http://www.qinqishuhua.org/show-217-55-1.html'
    r=requests.get(link,verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    zhengwen=str(soup.find('div','content').find('div')).strip('<div>').strip('</div>').replace('<font size="2">','').replace('</font>','')
    return zhengwen

def shicilink(link):
    #print link
    shici=[]
    r=requests.get(link,verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    tlist=soup.find('div','searchlist')
    sp2=BeautifulSoup(str(tlist),'lxml')
    tl=sp2.find_all('li')
    for i in tl:
        dic={}
        dic['title']=i.find('a').text
        dic['author']=i.find('span').text
        dic['link']=i.find('a')['href']
        #dic['content']=shicicontent(i.find('a')['href'])
        shici.append(dic)
        #print dic['title']
    return shici
def music(link):
    mlist=[]
    r=requests.get(link,verify=False)
    content=r.content
    soup=BeautifulSoup(content,'lxml')
    items=soup.find_all('li','select')
    for item in items:
        dic={}
        dic['title']=item.find('span','title').text
        dic['url']=item.find('span','title').find('a')['href'].replace('dq360','xbolo')
        dic['artist']=item.find('span','artist').text
        dic['num']=item.find('span','num').text
        mlist.append(dic)
    return mlist
if  __name__=='__main__':
    lss=shicilink('http://www.qinqishuhua.org/list-215-1.html')
    for i in lss:
        print(i)
