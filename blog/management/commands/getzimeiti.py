#coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
import os
import time
from  blog.robot import *
from blog.models import zmt


class Command(BaseCommand):
    def handle(self, *args, **options):
        for m in range(1,3):
            meitilist=zimeiti(m)
            for dic in meitilist:
                try:
                    a=zmt.objects.get_or_create(
                        zid=dic['zid'],
                        des=dic['des'],
                        title=dic['title'],
                        tag=dic['tag'],
                        picurl=dic['img'],
                        url=dic['url'],
                        author=dic['author'],
                        date=dic['date']
                    )
                except Exception:
                    pass     
        print('over')

