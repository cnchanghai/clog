#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.robot import *
from blog.models import technews


class Command(BaseCommand):
    def handle(self, *args, **options):
        link='http://tech.163.com'
        newslist=new163(link)
        for i in newslist:
            try:
                a=technews.objects.get_or_create(tag=i['tag'],title=i['title'],link=i['link'],time=i['time'],img=i['img'])
            except Exception as e:
                print(e) 
        print('tech news 163 over')

