#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import hashlib
from  blog.robot import yaoyans
from blog.models import yaoyan


class Command(BaseCommand):
    def handle(self, *args, **options):
        catalist=['pyxw','gzdt','zjsj','rdgz']
        for i in catalist:
            ylist=yaoyans(i,0)
            for item in ylist:
                try:
                    a=yaoyan.objects.get_or_create(
                        title=item['title'],
                        date=item['date'],
                        url=item['url'],
                        cata=i
                    )
                except Exception as e:
                    pass
            print('page  '+str(i)+'   is  ok')
