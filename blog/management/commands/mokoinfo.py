#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import hashlib
from  blog.moko import *
from blog.models import mtbziliao,mtbpic


class Command(BaseCommand):
    def handle(self, *args, **options):
        mtblist=mtbinfo()
        for item in mtblist:
            a=mtbziliao.objects.get_or_create(
                uid=item[0],
                uname=item[1],
                shengao=item[2],
                zhongliang=item[3],
                xiongwei=item[4],
                yaowei=item[5],
                tunwei=item[6],
                xiema=item[7],
                fase=item[8],
                yanjing=item[9],
            )
            piclist=mtbtu(item[0])
            for picurl in piclist:
                b=mtbpic.objects.get_or_create(uid=item[0],picurl=picurl)
            print(item[0]+'   is  ok')

