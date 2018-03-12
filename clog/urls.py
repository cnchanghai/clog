"""clog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_v

urlpatterns = (
    url(r'^moko.php/detail=(?P<uid>.+)$',blog_v.mokodetail,name='mokodetail'),
    url(r'^moko.php/(?P<page>\d+)$',blog_v.moko,name='moko'),
    url(r'^zmt.php/(?P<page>\d+)$',blog_v.zimeiti,name='zmt'),
    url(r'^r.html$',blog_v.resume,name='resume'),
    url(r'^technew.php/(?P<page>\d+)$',blog_v.technew,name='technew'),
    url(r'^piyao.php/(?P<cata>.+)/(?P<page>\d+)$',blog_v.piyao,name='piyao'),
    url(r'^music.php/(?P<cata>.+)$',blog_v.music,name='music'),
    url(r'^shici.php/(?P<cata>.+)/(?P<page>\d+)$',blog_v.shici,name='shici'),
    url(r'^shici.php/(?P<sid>\d+)$',blog_v.shicidetail,name='shicidetail'),
    url(r'^lishi$',blog_v.nolishi,name='nolishi'),
    url(r'^lishi.php/(?P<m>\d+)/(?P<d>\d+)$',blog_v.lishi,name='lishi'),
    url(r'^lishi.php/detail=(?P<id>\d+)$',blog_v.lishidetail,name='lishidetail'),
    url(r'^xiaohua.php/(?P<page>\d+)$', blog_v.xiaohua, name='xiaohua'),
    url(r'^$', blog_v.home, name='home'),
    url(r'^admin', admin.site.urls),
    url(r'^wechat.php$', blog_v.wechat, name='wechat'),
    url(r'^live.php/(?P<cata>.+)',blog_v.gamelive,name='live'),
    url(r'^movie/nowplay.php$',blog_v.movie_nowplay,name='movie_nowplay'),
    url(r'^movie/laterplay.php$',blog_v.movie_laterplay,name='movie_laterplay'),
    url(r'^movie/suggest.php$',blog_v.movie_suggest,name='movie_suggest'),
    url(r'^movie/tvshow.php$',blog_v.movie_tvshow,name='movie_tvshow'),

)
