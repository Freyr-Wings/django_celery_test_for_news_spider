from django.conf.urls import url
from django.contrib import admin

from .views import (
    news_list,
    news_detail,
    )


urlpatterns = [
    url(r'^$',news_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$',news_detail,name='detail'),
]