#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from blog.gamemix import *
from blog.models import gamelist

class Command(BaseCommand):
    def handle(self, *args, **options):
        gname=['hearthstone','lol','tvgame','girl','wangzhe','jdqs']
        zhanqinames=['chns/blizzard/how','games/lol','games/danji','games/xindong','games/wangzherongyao','games/pubg']
        huyanames=['393','lol','1964','2168','wzry','2793']
        douyunames=['how','lol','tvgame','yz','wzry','jdqs']
        pandanames=['hearthstone','lol','zhuji','yzdr','kingglory','pubg']
        quanminnames=['hearthstone','lol','tvgame','beauty','wangzhe','juediqiusheng']
        ccnames=['1005','','9022','65005','','']
        j=0
        game_time=float(time.time())
        #delete=gamelist.objects.filter(platform='cc').delete()
        #for ccname in ccnames:
        #    if ccname!='': 
        #        try:
        #            ccgame=cc163(ccname)
        #            for i in ccgame:
        #                insert=gamelist(platform='cc',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
        #                insert.save()
        #        except Exception, e:
        #            print gname[j]+'  cc is error'
        #    j+=1
        #print 'ccover'
        #delete=gamelist.objects.filter(platform='cc').delete()
        #for ccname in ccnames:
        #    if ccname!='': 
        #        try:
        #            ccgame=cc163(ccname)
        #            for i in ccgame:
        #                insert=gamelist(platform='cc',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
        #                insert.save()
        #        except Exception as e:
        #            print(gname[j]+'  cc is error')
        #    j+=1
        #print('ccover')



        j=0
        game_time=float(time.time())
        delete=gamelist.objects.filter(platform='douyu').delete()
        for douyuname in douyunames:              
            try:
                douyugame=douyu(douyuname)
                for i in douyugame:
                    insert=gamelist(platform='douyu',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                    insert.save()
            except Exception as e:
                print(gname[j]+'  douyu is error')
            j+=1  
        print('douyuover')

        delete=gamelist.objects.filter(platform='huya').delete()
        j=0
        for huyaname in huyanames:
              
            try:
                huyagame=huya(huyaname)
                for i in huyagame:
                    insert=gamelist(platform='huya',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                    insert.save()
            except Exception as  e:
                print(gname[j]+' huya is error')
            j+=1  
        print('huya over')
        game_time=float(time.time())
        delete=gamelist.objects.filter(platform='panda').delete()
        j=0
        for pandaname in pandanames:
            try:
                pandagame=panda(pandaname)
                for i in pandagame:
                    insert=gamelist(platform='panda',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                    insert.save()
            except Exception as  e:
                print(gname[j]+' panda is error')  
            j+=1
        print('panda over')
        j=0
        #delete=gamelist.objects.filter(platform='quanmin').delete()
        #for quanminname in quanminnames:
        #    try:
        #        quanmingame=quanmin(quanminname)
        #        for i in quanmingame:
        #            insert=gamelist(platform='quanmin',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
        #            insert.save()
        #    except Exception as  e:
        #        print(gname[j]+'  quanmin is error')  
        #    j+=1
        #print('quanmin over')

        game_time=float(time.time())
        delete=gamelist.objects.filter(platform='zhanqi').delete()
        j=0
        for zhanqiname in zhanqinames:
              
            try:
                zhanqigame=zhanqi(zhanqiname)
                for i in zhanqigame:
                    insert=gamelist(platform='zhanqi',game_name=gname[j],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                    insert.save()
            except Exception as  e:
                print(gname[j]+' zhanqi is error')
            j+=1  
        print('zhanqi over')

