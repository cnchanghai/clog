#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.func import *
from blog.models import fulipic


class Command(BaseCommand):
    def handle(self, *args, **options):
        #for m in range(1,30):
        #    print('============= page  '+str(m)+'   ============')
        qiubailist=fuli(0)
        for i in qiubailist:
            try:
                a=fulipic.objects.get_or_create(picurl=i)
            except:
                tmp = os.popen('systemctl start mariadb').readlines()
        print('over')

