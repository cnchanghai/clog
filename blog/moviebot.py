#coding=utf8
import requests
import selenium.webdriver
from bs4 import BeautifulSoup
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def nowplay():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    movie_list=[]
    url='https://movie.douban.com/cinema/nowplaying/suzhou/'
    r = requests.get(url,verify=False,headers=headers)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    #print soup
    live_list=soup.find_all('li',attrs = {'class' : 'list-item'})
    for i in live_list:
        try:
            all_game=i
            #print (all_game)
            movie_type=all_game['data-category']
            #print (movie_type)
            if movie_type=='nowplaying':
                movie_name=all_game.find('a',attrs = {'data-psource' : 'title'}).text.strip()

                movie_link=all_game.find('a',attrs = {'data-psource' : 'title'})['href']
                #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
                movie_actor=all_game['data-actors']
                movie_director=all_game['data-director']
                movie_time=all_game['data-duration']
                movie_region=all_game['data-region']
                movie_release=all_game['data-release']
                movie_score=all_game['data-score']
                movie_pic=all_game.find('img')['src']
                movie_dic={}
                movie_dic['movie_name']=movie_name
                movie_dic['movie_link']=movie_link
                movie_dic['movie_actor']=movie_actor
                movie_dic['movie_director']=movie_director
                movie_dic['movie_time']=movie_time
                movie_dic['movie_region']=movie_region
                movie_dic['movie_release']=movie_release
                movie_dic['movie_score']=movie_score
                movie_dic['movie_pic']=movie_pic
                movie_list.append(movie_dic)
                #break
            else:
                pass
        except Exception as e:
            print(e)
    return movie_list


def tvshow():
    tv_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    url='https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    driver.get(url)
    time.sleep(4)
    content=driver.page_source
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('a',attrs = {'class':'item'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i
            #print (i)
            tv_name=all_game.find('p').text.strip().split()[0]
            tv_link=all_game['href']
            tv_score=all_game.find('strong').text.strip()
            tv_pic=all_game.find('img')['src']
            tv_dic={}
            tv_dic['tv_name']=tv_name
            tv_dic['tv_link']=tv_link
            tv_dic['tv_score']=tv_score
            tv_dic['tv_pic']=tv_pic
            tv_list.append(tv_dic)
            #print (tv_list)
            #break
        except Exception as e:
            print(e)
    return tv_list



def laterplay():
    movie_list=[]
    url='https://movie.douban.com/cinema/later/suzhou/'
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('div',attrs = {'class' : 'item mod '})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i

            #print (all_game)
            movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})

            movie_name=all_game.find('a',attrs = {'class' : ''}).text.strip()

            movie_link=all_game.find('a',attrs = {'class' : ''})['href']

            #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
            movie_pic=all_game.find('img',attrs = {'class' : ''})['src']
            movie_time=all_game.find_all('li',attrs = {'class' : 'dt'})[0].text.strip()
            movie_type=all_game.find_all('li',attrs = {'class' : 'dt'})[1].text.strip()
            movie_region=all_game.find_all('li',attrs = {'class' : 'dt'})[2].text.strip()
            movie_people=all_game.find_all('li',attrs = {'class' : 'dt'})[3].text.strip()
            movie_people=float(''.join(list(movie_people)[0:-3]))
	    #print movie_people
            if movie_preview != None:
                movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})['href']
            else:
                movie_preview=''
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_pic']=movie_pic
            movie_dic['movie_time']=movie_time
            movie_dic['movie_type']=movie_type
            movie_dic['movie_region']=movie_region
            movie_dic['movie_people']=movie_people
            movie_dic['movie_preview']=movie_preview
            movie_list.append(movie_dic)

            #break
        except Exception as e:
            print(e)


    live_list=soup.find_all('div',attrs = {'class' : 'item mod odd'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i

            #print (all_game)
            movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})

            movie_name=all_game.find('a',attrs = {'class' : ''}).text.strip()

            movie_link=all_game.find('a',attrs = {'class' : ''})['href']

            #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
            movie_pic=all_game.find('img',attrs = {'class' : ''})['src']
            movie_time=all_game.find_all('li',attrs = {'class' : 'dt'})[0].text.strip()
            movie_type=all_game.find_all('li',attrs = {'class' : 'dt'})[1].text.strip()
            movie_region=all_game.find_all('li',attrs = {'class' : 'dt'})[2].text.strip()
            movie_people=all_game.find_all('li',attrs = {'class' : 'dt'})[3].text.strip()
            movie_people=int(''.join(list(movie_people)[0:-3]))
	    #print movie_people
            if movie_preview != None:
                movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})['href']
            else:
                movie_preview=''
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_pic']=movie_pic
            movie_dic['movie_time']=movie_time
            movie_dic['movie_type']=movie_type
            movie_dic['movie_region']=movie_region
            movie_dic['movie_people']=movie_people
            movie_dic['movie_preview']=movie_preview
            movie_list.append(movie_dic)

            #break
        except Exception as e:
            print(all_game)

    return movie_list


def movie_suggest():
    movie_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    url='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    driver.get(url)
    time.sleep(4)
    content=driver.page_source
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('a',attrs = {'class':'item'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i
            #print(i)
            movie_name=all_game.find('p').text.strip().split()[0]
            movie_link=all_game['href']
            movie_score=all_game.find('strong').text.strip()
            movie_pic=all_game.find('img')['src']
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_score']=movie_score
            movie_dic['movie_pic']=movie_pic
            movie_list.append(movie_dic)
            #print (tv_list)
            #break
        except Exception as e:
            print(e)
    return movie_list





if __name__=="__main__":
    #res=nowplay()
    res=laterplay()
    for i in res:
        print(i)
