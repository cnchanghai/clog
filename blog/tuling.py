#coding=utf8
import requests
from django.shortcuts import render_to_response
from bs4 import BeautifulSoup
import random


def tuling1(info,userid):
    key='8906be7b367341199279c21462391cd0'
    url='http://www.tuling123.com/openapi/api'
    #info='苏州'
    postdata={
        'key':key,
        'info':info,
	'userid':userid
             }

    r = requests.post(url, data = postdata)


    result=r.content

    result=eval(result)
    message_type= result['code']
    #print (message_type)
    #print type(message_type)
    if message_type==100000:
        tuling_reply={}
        tuling_reply['code']=(result['code'])
        tuling_reply['content']=(result['text']).strip()
        return tuling_reply
    if message_type==200000:
        #print (result['text'])
        #print (result['url'])
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['description']=(result['text'])
        tuling_reply['title'] = (result['text'])
        tuling_reply['url'] = (result['url'])
        return tuling_reply
    if message_type==302000:
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['text'] = (result['text'])
        news=result['list']
        tuling_reply['title1'] = news[0]['article']
        tuling_reply['picurl1'] = news[0]['icon']
        tuling_reply['description1'] = news[0]['source']
        tuling_reply['url1'] = news[0]['detailurl']
        tuling_reply['title2'] = news[1]['article']
        tuling_reply['picurl2'] = news[1]['icon']
        tuling_reply['description2'] = news[1]['source']
        tuling_reply['url2'] = news[1]['detailurl']
        return  tuling_reply

    if message_type==308000:
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['text'] = (result['text'])
        caipu = result['list']
        tuling_reply['title1']=caipu[0]['name']
        tuling_reply['picurl1']=caipu[0]['icon']
        tuling_reply['description1'] = caipu[0]['info']
        tuling_reply['url1'] = caipu[0]['detailurl']
        tuling_reply['title2'] = caipu[1]['name']
        tuling_reply['picurl2'] = caipu[1]['icon']
        tuling_reply['description2'] = caipu[1]['info']
        tuling_reply['url2'] = caipu[1]['detailurl']
        tuling_reply['title3'] = caipu[2]['name']
        tuling_reply['picurl3'] = caipu[2]['icon']
        tuling_reply['description3'] = caipu[2]['info']
        tuling_reply['url3'] = caipu[2]['detailurl']
        tuling_reply['title4'] = caipu[3]['name']
        tuling_reply['picurl4'] = caipu[3]['icon']
        tuling_reply['description4'] = caipu[3]['info']
        tuling_reply['url4'] = caipu[3]['detailurl']
        return tuling_reply
def Tlrobot(dic):
    data={}
    info = dic['Content']
    userid = dic['MsgId']
    result = tuling1(info, userid)
    if result['code'] == 100000:
        dic['Content'] = result['content']
        data['muban'] ='reply_message.html'
        #return render_to_response('reply_message.html', dic)
    elif result['code'] == 200000:
        dic['Title'] = result['title']
        dic['Description'] = result['description']
        dic['Url'] = result['url']
        dic['PicUrl'] = ''
        #return render_to_response('reply_link.html', dic)
        data['muban'] = 'reply_link.html'
    elif result['code'] == 302000:
        dic['title1'] = result['title1']
        dic['description1'] = result['description1']
        dic['picurl1'] = result['picurl1']
        dic['url1'] = result['url1']
        dic['title2'] = result['title2']
        dic['description2'] = result['description2']
        dic['picurl2'] = result['picurl2']
        dic['url2'] = result['url2']
        data['muban'] = 'reply_news.html'
        #return render_to_response('reply_news.html', dic)
    elif result['code'] == 308000:
        dic['title1'] = result['title1']
        dic['description1'] = result['description1']
        dic['picurl1'] = result['picurl1']
        dic['url1'] = result['url1']
        dic['title2'] = result['title2']
        dic['description2'] = result['description2']
        dic['picurl2'] = result['picurl2']
        dic['url2'] = result['url2']
        dic['title3'] = result['title3']
        dic['description3'] = result['description3']
        dic['picurl3'] = result['picurl3']
        dic['url3'] = result['url3']
        dic['title4'] = result['title4']
        dic['description4'] = result['description4']
        dic['picurl4'] = result['picurl4']
        dic['url4'] = result['url4']
        dic['MsgType'] = 'news'
        data['muban'] = 'reply_caipu.html'
        #return render_to_response('reply_caipu.html', dic)
    data['dat'] = dic
    return data
if __name__=="__main__":
    info='王大可这个名字怎么样'
    userid='1234456'
    print(tuling1(info,userid))


