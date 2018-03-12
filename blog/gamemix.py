#coding=utf8
import requests
import selenium.webdriver
from bs4 import BeautifulSoup
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def douyu(douyugame):
    game_list=[]
    url='HTTPs://www.douyu.com/directory/game/'+douyugame
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'data-cid' : True})
    for i in live_list:
        try:
            all_game=i.find('a')
            game_count=all_game.find('span',attrs = {'class' : 'dy-num fr'}).text
            if '.' in game_count:
                game__count=float(game_count[0:-1])*10000
            if float(game_count)>8000:
                game_link='https://www.douyu.com'+all_game['href']
                game_title=all_game['title']
                game_picture= all_game.find('img')['data-original']
                game_nickname=all_game.find('span',attrs = {'class' : 'dy-name ellipsis fl'}).text
                #print all_game
                #print game_link
                #print game_title
                #print game_picture
                #print game_nickname
                #print game_count
                #print '\n'
                #break
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)

        except Exception:
            pass
#    print game_list
    return game_list
def panda(pandagame):
    game_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(50)
    driver.set_page_load_timeout(50)
    url='http://www.panda.tv/cate/'+pandagame
    driver.get(url)
    content=driver.page_source
    #r = requests.get(url)
    #content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'video-list-item video-no-tag video-no-cate '})
    #print live_list[-1]
    for i in live_list:
        try:
            all_game=i.find('a')
            #print all_game
            game_count=i.find('span',attrs = {'class' : 'video-number'}).text
            game_count=game_count[0:-1]
            if '.' in game_count:
                game_count=float(game_count)*10000

            #print game_count
            if  game_count>8000:
                game_link='http://www.panda.tv'+all_game['href']
                game_title=i.find('span',attrs = {'class' : 'video-title'})['title']
                game_picture= i.find('img',attrs = {'class' : 'video-img video-img-lazy'})['data-original']
                game_nickname=i.find('span',attrs = {'class' : 'video-nickname'}).text
                #print all_game
                #print game_link
                #print game_nickname
                #print game_title
                #print game_picture
                #print game_count
                #print '\n'
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
          #  break
        except Exception:
            pass
 #   print game_list
    return game_list
def huya(huyagame):
    game_list=[]
    url='http://www.huya.com/g/'+huyagame
    #driver = selenium.webdriver.PhantomJS()
    #driver.implicitly_wait(40)
    #driver.set_page_load_timeout(40)
    #driver.get(url)
    #time.sleep(5)
    #content=driver.page_source
    r = requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'game-live-item'})
    for i in live_list:
        try:
            all_game=i
            #print all_game
            game_count=all_game.find('i',attrs = {'class' : 'js-num'}).text
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            if  float(game_count)>8000:
                #game_link=all_game.find('a',attrs = {'class' : 'video-info new-clickstat'})['href']
                game_link=all_game.find('a')['href']
                game_title=all_game.find('a',attrs = {'class' : 'title new-clickstat'}).text.strip()
                game_picture= all_game.find('img',attrs = {'class' : 'pic'})['data-original']
                game_nickname=all_game.find('i',attrs = {'class' : 'nick'}).text
                #print all_game
                #print game_link
                #print game_nickname
                #print game_title
                #print game_picture
                #print game_count
                #print '\n'
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
		#break
        except Exception:
            pass
        #break
    #print game_list
    return game_list

def zhanqi(zhanqigame):
    game_list=[]
    url='https://www.zhanqi.tv/'+zhanqigame
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'data-room-id' : True})
    for i in live_list:
        try:
            all_game=i.find('a')
            game_count=all_game.find('span',attrs = {'class' : 'dv'}).text
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            if float(game_count)>8000:
                game_link='https://www.zhanqi.tv'+all_game['href']
                game_title=all_game.find('img')['alt']
                game_picture= all_game.find('img')['src']
                game_nickname=all_game.find('span',attrs = {'class' : 'anchor anchor-to-cut dv'}).text
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)

        except Exception:
            pass
    #print game_list
    return game_list

def quanmin(quanminname):
    game_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(50)
    driver.set_page_load_timeout(50)
    url='http://www.quanmin.tv/game/'+quanminname
    driver.get(url)
    content=driver.page_source
    soup = BeautifulSoup(content,"lxml")
    #print soup
    live_list=soup.find_all('li',attrs = {'class' : 'list_w-video'})
    for i in live_list:
        try:
            #print i
            all_game=i.find('a')
            game_count=i.find('span',attrs = {'class' : 'common_w-card_views-num'}).text
            game_count=str(game_count).strip().replace(',','')
            #print all_game
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            #print  game_count
            if  float(game_count)>8000:
                game_nickname=i.find('span',attrs = {'class' : 'common_w-card_host-name'}).text.strip()
                game_link='http:'+all_game['href']
                #game_title=all_game.find('img',attrs = {'class' : 'w-video_thumb'})['alt']
                #game_picture= all_game.find('img',attrs = {'class' : 'w-video_thumb'})['src']
                game_title=i.find('p',attrs = {'class' : 'common_w-card_title'}).text.strip()
                game_picture= i.find('img',attrs = {'class' : 'common_w-card_cover'})['src']
                #print( all_game)
                #print(game_author.strip())
                #print (game_link)
                #print (game_title)
                #print (picture)
                #print (game_count)
                #print ('\n')
                #break
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
        except Exception as  e:
            #pass
            print(e)
    return game_list
def cc163(ccname):
    game_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(50)
    driver.set_page_load_timeout(50)
    url='http://cc.163.com/category/list/?gametype='+ccname
    driver.get(url)
    content=driver.page_source
    #print content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class':'game-item js-game-item'})
    for i in live_list:
        try:
            game_count=i.find('span',attrs = {'class' : 'right game-item-visitor'}).text.strip()
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            if game_count!='':
                game_link='http://cc.163.com'+i.find('a')['href']
                game_title=i.find('a',attrs={'class':'left game-item-title nick'}).text
                game_picture= i.find('img')['src']
                game_nickname=i.find('span',attrs = {'class' : 'game-item-nick nick'}).text
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                #print game_dic
                game_list.append(game_dic)
        except Exception as e:
            print(e)
    return game_list


if __name__=="__main__":
    douyuname='overwatch'
    pandaname='beauty'
    huyaname='2174'
    quanminname='overwatch'
    res=huya('hearthstone')
    for i in res:
        print(i)
