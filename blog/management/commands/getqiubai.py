#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.robot import *
from blog.models import qiubai


class Command(BaseCommand):
    def handle(self, *args, **options):
        for m in range(1,12):
            qiubailist=qiushi(m)
            for i in qiubailist:
                a=qiubai.objects.get_or_create(name=i['a'], content=i['c'])

        
        print('over')

