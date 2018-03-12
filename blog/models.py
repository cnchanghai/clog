from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class technews(models.Model):
    title=models.CharField(max_length=150,unique=True)
    tag=models.CharField(max_length=10)
    link=models.CharField(max_length=250)
    time=models.DateTimeField()
    img=models.CharField(max_length=250)
    def __unicode__(self):
        return self.title
class musiclist(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    cata=models.CharField(max_length=20)
    num=models.IntegerField()
    url=models.CharField(max_length = 250)
    def __unicode__(self):
        return self.title
class shicilist(models.Model):
    sid= models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    cata=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    content=models.TextField()
    def __unicode__(self):
        return self.title
class yaoyan(models.Model):
    title=models.CharField(max_length =150,unique=True)
    date=models.DateTimeField()
    cata=models.CharField(max_length =20,blank=True)
    url=models.CharField(max_length = 250)
    def __unicode__(self):
        return self.title
class zmt(models.Model):
    zid=models.IntegerField(unique=True)
    title=models.CharField(max_length = 50)
    des=models.CharField(max_length = 100)
    author=models.CharField(max_length = 20)
    date=models.CharField(max_length=20)
    tag=models.CharField(max_length = 12)
    picurl=models.CharField(max_length = 250)
    url=models.CharField(max_length = 100)
    def __unicode__(self):
        return self.title
class qiubai(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length = 50)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name
class lsjt(models.Model):
    id = models.AutoField(primary_key=True)
    year=models.CharField(max_length=15)
    month=models.CharField(max_length=15)
    day=models.CharField(max_length=15)
    title=models.CharField(max_length = 50)
    content=models.TextField()
    def __unicode__(self):
        return self.title
class mtbziliao(models.Model):
    uid=models.CharField(max_length=20,unique=True)
    uname=models.CharField(max_length=20)
    shengao=models.CharField(max_length=5)
    zhongliang=models.CharField(max_length=5)
    xiongwei=models.CharField(max_length=5)
    yaowei=models.CharField(max_length=5)
    tunwei=models.CharField(max_length=5)
    xiema=models.CharField(max_length=5)
    fase=models.CharField(max_length=10)
    yanjing=models.CharField(max_length=10)
    def __unicode__(self):
        return self.uid
class mtbpic(models.Model):
    uid=models.CharField(max_length=20)
    picurl=models.CharField(max_length=250)
    def __unicode__(self):
        return self.uid
class gamelist(models.Model):
    platform=models.CharField(max_length=10)
    game_name=models.CharField(max_length=20)
    game_link=models.CharField(max_length=100)
    game_title=models.CharField(max_length=100)
    game_picture=models.CharField(max_length=300)
    game_nickname=models.CharField(max_length=100)
    game_time=models.FloatField()
    game_count=models.FloatField()
    def __unicode__(self):
        return self.game_title
class movielist(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_link=models.CharField(max_length=100)
    movie_actor=models.CharField(max_length=100)
    movie_type=models.CharField(max_length=20)
    movie_director=models.CharField(max_length=50)
    movie_time=models.CharField(max_length=20)
    movie_region=models.CharField(max_length=50)
    movie_release=models.CharField(max_length=10)
    movie_score=models.FloatField()
    movie_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name
class laterlist(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_link=models.CharField(max_length=100)
    movie_pic=models.CharField(max_length=100)
    movie_time=models.CharField(max_length=20)
    movie_type=models.CharField(max_length=50)
    movie_region=models.CharField(max_length=20)
    movie_people=models.IntegerField()
    movie_preview=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name
class tvlist(models.Model):
    tv_name=models.CharField(max_length=100)
    tv_link=models.CharField(max_length=100)
    tv_score=models.FloatField()
    tv_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.tv_name
class moviesuggest(models.Model):
    movie_name=models.CharField(max_length=100)
    movie_link=models.CharField(max_length=100)
    movie_score=models.FloatField()
    movie_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name

admin.site.register(technews)
admin.site.register(shicilist)
admin.site.register(yaoyan)
admin.site.register(zmt)
admin.site.register(movielist)
admin.site.register(gamelist)
admin.site.register(mtbpic)
admin.site.register(mtbziliao)
admin.site.register(qiubai)
admin.site.register(lsjt)
admin.site.register(musiclist)
