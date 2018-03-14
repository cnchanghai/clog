# coding:utf-8
from blog.tuling import *
import hashlib
import time
from lxml import etree
from blog.parse import *
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.urls import reverse
from django.http import HttpResponse as HR
from blog.models import *

# Create your views here.
@csrf_exempt
def wechat(request):
    if request.method == "GET":
        token = 'cnchanghai'  # 填入你的 Token
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echoStr = request.GET.get("echostr", None)
        #tmpList = [token, timestamp, nonce]
        #tmpList.sort()
        #tmpstr = "%s%s%s" % tuple(tmpList)
        #tmpstr = hashlib.sha1(tmpstr).hexdigest()
        #if tmpstr == signature:
        if signature != None:
            return HR(request.GET.get('echostr', ''))
        else:
            return HR("<img src=\"/static/images/wechatqr.jpg\">")
    else:
        xml_str = request.body.decode('utf-8')
        xml = etree.fromstring(xml_str)
        messagetype = xml.find('MsgType').text
        if messagetype == 'text':
            dic = parse_message(xml)
            if dic['Content'].lower() == 'time' or dic['Content']==u'时间':
                buf=u'当前时间为：'+ str(time.ctime())+u'\nunix时间戳为:'+str(time.time())
                dic['Content'] =buf
                return render_to_response('reply_message.html', dic)
            elif dic['Content'].lower() == 'joke':
                xiaohua = random.choice(qiubai.objects.all())
                dic['Content'] = xiaohua.content
                return render_to_response('reply_message.html', dic)
            elif dic['Content']==u'模特'or'model'== dic['Content'].lower():
                maxrecord=mtbpic.objects.count()-1
                ranint=randint(0, maxrecord)
                mtpic=mtbpic.objects.all()[ranint]
                dic['Title']=u'美模图'
                dic['Description']=u'18岁以下，请在父母陪同下观看'
                dic['PicUrl']=mtpic.picurl
                #dic['Content']=u'18岁以下，请在父母陪同下观看'
                dic['Url']='http://www.xbolo.win'+reverse('mokodetail',kwargs={'uid':mtpic.uid})
                return render_to_response('reply_link.html', dic)
                #return render_to_response('reply_message.html',dic)
            elif dic['Content']==u'福利':
                maxrecord=fulipic.objects.count()-1
                ranint=randint(0, maxrecord)
                mtpic=fulipic.objects.get(id=ranint)
                dic['Title']=u'福利图'
                dic['Description']=u'18岁以下，请在父母陪同下观看'
                dic['PicUrl']=mtpic.picurl
                dic['Url']='http://www.xbolo.win'+reverse('fulitu',kwargs={'picid':mtpic.id})
                return render_to_response('reply_link.html', dic)
            elif dic['Content'].lower()=='today' or dic['Content']==u'今天':
                txt=''
                m=str(time.strftime('%m'))
                if '0'==m[0]:m=m.strip('0')
                d=str(time.strftime('%d'))
                if '0'==d[0]:d=d.strip('0')
                daylist=lsjt.objects.filter(month=m,day=d).values('year','title')
                for i in daylist:
                    txt=txt+i['year']+u'年--'+i['title']+'\n'
                dic['Content']=txt
                return render_to_response('reply_message.html',dic)
            elif  'help'== dic['Content'].lower() or u'帮助'==dic['Content'] or u'?' in dic['Content']:
                dic['Content']='感谢您的关注！\n输入“帮助”或“help”查看相应命令单\n输入“模特”或“model”查看模特图片\n输入“福利” 可以看福利照片\n输入”快递查询“可以查询快递\n输入“time” 查看当前时间\n输入“joke”或者“笑话”查看笑话\n输入“today”或“今天”可以查看历史上的今天\n其他条目由图灵机器人为您服务\n网站：www.xbolo.win  和 www.lichanghai.cn 期待您的光临'
                return render_to_response('reply_message.html',dic)
            else:
                data=Tlrobot(dic)#图灵机器人
                return render_to_response(data['muban'],data['dat'])
        elif messagetype=='image':
            dic=parse_image(xml)
            return render_to_response('reply_image.html',dic)
        elif messagetype=='voice':
            dic=parse_voice(xml)
            return render_to_response('reply_voice.html',dic)


def xiaohua(request,page):
    page=int(page)
    xianshi=25
    max_record= qiubai.objects.count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('xiaohua',kwargs={"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    XiaohuaList=qiubai.objects.all().order_by("-id")[xianshi*(page-1):en_record]
    return render(request, 'xiaohua.html', {'XiaohuaList': XiaohuaList, 'npage': npage, 'ppage': ppage, })
def technew(request,page):
    page=int(page)
    xianshi=20
    max_record= technews.objects.count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('technew',kwargs={"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    newslist=technews.objects.all().order_by("-time")[xianshi*(page-1):en_record]
    return render(request, 'technew.html', {'newslist': newslist, 'npage': npage, 'ppage': ppage, })

def mokodetail(request,uid):
    mtinfo=mtbziliao.objects.get(uid=uid)
    mtpic=mtbpic.objects.filter(uid=uid)
    return render(request,'mokodetail.html',{'mtinfo':mtinfo,'mtpic':mtpic,})
def fulitu(request,picid):
    onepic=fulipic.objects.get(id=picid)
    return render(request,'fulitu.html',{'onepic':onepic,})
def moko(request,page):
    xianshi=12
    page=int(page)
    max_record=mtbziliao.objects.count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('moko',kwargs={"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    mtlist1=mtbziliao.objects.all()[xianshi*(page-1):en_record]
    mtlist=[]
    for item in mtlist1:
        dic={}
        dic['uid']=item.uid
        dic['uname']=item.uname
        dic['picurl']=mtbpic.objects.filter(uid=item.uid)[0].picurl
        mtlist.append(dic)
    return render(request,'moko.html',{'mtlist':mtlist,'npage':npage,'ppage':ppage,})
def home(request):
    string = u"感谢您的关注，目前网站正在建设中<br><img src=\"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3312395508,4066513042&fm=26&gp=0.jpg\"> "
    return render(request, 'index.html', {'string': string})


def nolishi(request):
    m=str(time.strftime('%m'))
    if '0'==m[0]:m=m.strip('0')
    d=str(time.strftime('%d'))
    if '0'==d[0]:d=d.strip('0')
    #daylist = lsjt.objects.filter(month=m, day=d).values('year', 'month', 'day', 'mdtxt', 'title')
    #return render(request, 'lishi.html', {'daylist': daylist})
    return  redirect(reverse("lishi", kwargs={"m":m, "d":d}))
def lishi(request,m,d):
    daylist=lsjt.objects.filter(month=m,day=d).values('year','month','day','id','title')
    return render(request, 'lishi.html', {'daylist':daylist})
def lishidetail(request,id):
    text=lsjt.objects.get(id=id)
    return render(request, 'lishidetail.html', {'text': text})

def gamelive(request,cata):
    result=''
    if cata=='hot':result=gamelist.objects.all().order_by('-game_count')[0:60]
    else:result=gamelist.objects.filter(game_name=cata).order_by('-game_count')
    return render(request,'gamelive.html',{'result':result,'cata':cata})
def music(resquest,cata):
    mlist=musiclist.objects.filter(cata=cata)
    return render_to_response('music.html',{'mlist':mlist,'cata':cata})
def shici(request,cata,page):
    xianshi=30
    page=int(page)
    max_record=0
    max_record=shicilist.objects.filter(cata=cata).count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('shici',kwargs={"cata":cata,"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    mtlist=shicilist.objects.filter(cata=cata).values('title','author','sid')[xianshi*(page-1):en_record]
    return render(request,'shici.html',{'mtlist':mtlist,'npage':npage,'ppage':ppage,'cata':cata,})
def shicidetail(request,sid):
    txt=shicilist.objects.get(sid=sid)
    cata=txt.cata
    return render(request,'shicidetail.html',{'txt':txt,'cata':cata})



def movie_nowplay(request):
    result=movielist.objects.filter(movie_type='nowplaying')
    dic={'result':result}
    return render_to_response('movie_nowplay.html',dic)


def movie_tvshow(request):
    result=tvlist.objects.all
    dic={'result':result}
    return render_to_response('movie_tvshow.html',dic)

def movie_suggest(request):
    result=moviesuggest.objects.all
    dic={'result':result}
    return render_to_response('movie_suggest.html',dic)

def movie_laterplay(request):
    result=laterlist.objects.all
    dic={'result':result}
    return render_to_response('movie_laterplay.html',dic)
def resume(request):
    return render_to_response('resume.html')
def zimeiti(request,page):
    xianshi=12
    page=int(page)
    max_record=zmt.objects.count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('zmt',kwargs={"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    zlist=zmt.objects.all().order_by('-zid')[xianshi*(page-1):en_record]
    return render(request,'zmt.html',{'zlist':zlist,'npage':npage,'ppage':ppage,})
def piyao(request,cata,page):
    xianshi=25
    page=int(page)
    max_record=0
    if cata=='all':
        max_record=yaoyan.objects.count()
    else:
        max_record=yaoyan.objects.filter(cata=cata).count()
    max_page=max_record/xianshi
    if max_record%xianshi>0:
        max_page+=1
    if page>max_page or page<1:
        return redirect(reverse('piyao',kwargs={"cata":cata,"page":1}))
    npage=page+1
    ppage=page-1
    en_record=page*xianshi
    if en_record>=max_record:
        en_record=max_record
        npage=0
    if npage>max_page:
        npage=0
    mtlist=[]
    if cata=="all":
        mtlist=yaoyan.objects.all().order_by('-date')[xianshi*(page-1):en_record]
    else:
        mtlist=yaoyan.objects.filter(cata=cata).order_by('-date')[xianshi*(page-1):en_record]
    return render(request,'piyao.html',{'mtlist':mtlist,'npage':npage,'ppage':ppage,'cata':cata,})

