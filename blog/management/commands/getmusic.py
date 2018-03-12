#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.robot import *
from blog.models import musiclist


class Command(BaseCommand):
    def handle(self, *args, **options):
        ms=['new','hot','classic','internet']
        for urls in ms:
            a=musiclist.objects.filter(cata=urls).delete()
            link='http://music.so.com/top/'+urls+'.html'
            print('start: '+link)
            mlist=music(link)
            for i in mlist:
                try:
                    a=musiclist.objects.get_or_create(title=i['title'],num=i['num'],cata=urls,artist=i['artist'],url=i['url'])
                except Exception:
                    pass
            print('done:  '+link)
        print('over')
