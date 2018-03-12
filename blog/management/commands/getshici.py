#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.robot import *
from blog.models import shicilist


class Command(BaseCommand):
    def handle(self, *args, **options):
        wzlm=[
            {'name':'tangshi','pages':12,'id':217},
            {'name':'songci','pages':12,'id':218},
            {'name':'xiaoxue','pages':2,'id':215},
            {'name':'yuanqu','pages':5,'id':220}
        ]
        for i in wzlm:
            for j in range(1,i['pages']):       
                link='http://www.qinqishuhua.org/list-'+str(i['id'])+'-'+str(j)+'.html'
                print(link)
                shici=shicilink(link)
                for k in shici:
                    try:
                        print(k['title'])
                        content=shicicontent(k['link'])
                        a=shicilist.objects.get_or_create(title=k['title'],author=k['author'],content=content,cata=i['name'])
                    except Exception:
                        pass
        print('over')
