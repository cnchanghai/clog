#coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import random
def fuli(dic):
    page=random.randint(1,89)
    pages='http://jandan.net/ooxx/page-'+str(page)+'#comments'
    r = requests.get(pages, verify=False)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
    linklist = soup.find_all('div', 'text')
    a=linklist[random.randint(0,len(linklist))]
    b=a.find('img').get('src')
    b='http:'+b
    dic['Title']=u'福利图'
    dic['Description']=u'18岁以下，请在父母陪同下观看'
    dic['PicUrl']=b
    dic['Url']=b
    return dic
