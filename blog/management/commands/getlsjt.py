#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import hashlib
from  blog.robot import *
from blog.models import lsjt


class Command(BaseCommand):
    def handle(self, *args, **options):
        a=[31,29,31,30,31,30,31,31,30,31,30,31]
        m=1
        for j in a:   
            for d in range(j):
                lslist=lssdjt(m,d+1)
                for i in lslist:
                    text=i['content'].encode('utf8')
                    a=lsjt.objects.get_or_create(month=m,title=i['title'],day=d+1,year=i['year'],content=i['content'])
                print(m,'/',d+1,'over')
            m=m+1

