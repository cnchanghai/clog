#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from blog.moviebot import *
from blog.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=movielist.objects.all().delete()
        type=''
        nowplaying=nowplay()
        for i in nowplaying:
            insert=movielist(movie_name=i['movie_name'],movie_type='nowplaying',movie_link=i['movie_link'],movie_actor=i['movie_actor'],movie_director=i['movie_director'],movie_time=i['movie_time'],movie_region=i['movie_region'],movie_release=i['movie_release'],movie_score=float(i['movie_score']),movie_pic=i['movie_pic'])
            insert.save()   
        print('movielist over')
        #tv list start
        delete=tvlist.objects.all().delete()
        type=''
        tv=tvshow()
	#print tv
        for i in tv:
            insert=tvlist(tv_name=i['tv_name'],tv_link=i['tv_link'],tv_score=float(i['tv_score']),tv_pic=i['tv_pic'])
            insert.save()
        
        print('tvlist over')
        #movie suggest start
        delete=moviesuggest.objects.all().delete()
        type=''
        movie=movie_suggest()
	#print tv
        for i in movie:
            insert=moviesuggest(movie_name=i['movie_name'],movie_link=i['movie_link'],movie_score=float(i['movie_score']),movie_pic=i['movie_pic'])
            insert.save()
        
        print('movie suggest over')

        
        delete=laterlist.objects.all().delete()
        type=''
        laterplaying=laterplay()
        for i in laterplaying:
            insert=laterlist(movie_name=i['movie_name'],movie_link=i['movie_link'],movie_pic=i['movie_pic'],movie_time=i['movie_time'],movie_type=i['movie_type'],movie_region=i['movie_region'],movie_people=i['movie_people'],movie_preview=i['movie_preview'])
            insert.save()
        
        print('later play over')
        print('all over')

