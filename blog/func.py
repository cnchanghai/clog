#coding:utf-8 -*-
from bs4 import BeautifulSoup
import time
import requests
import selenium.webdriver
from datetime import datetime,timedelta
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def fuli(dic):
    page=dic
    pages='http://jandan.net/ooxx/page-'+str(page)+'#comments'
    #r = requests.get(pages, verify=False)
    driver = selenium.webdriver.PhantomJS()
    driver.get(pages)
    content=driver.page_source
    #content = r.content
    #print( content)
    soup = BeautifulSoup(content, 'lxml')
    linklist = soup.find_all('div', 'text')
    #a=linklist[random.randint(0,len(linklist))]
    piclist=[]
    for a in linklist:
        b=a.find('img').get('src')
        if '.gif' in b:
            continue
        else:piclist.append(b)
    return piclist
if __name__=='__main__':
    for i in range(1,49):
        print('============page '+str(i)+' ==============')
        pic=fuli(i)
        print(pic)
        print('sleep20')
        time.sleep(20)
