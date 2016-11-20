from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import News
import urllib,urllib2
import re
import sys
# Create your views here.

def news_list(request):
    newsset = News.objects.all()
    return render(request, "base.html",{"title_list":newsset})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    context={
        "news":news
    }
    return render(request, "news_detail.html", context)
