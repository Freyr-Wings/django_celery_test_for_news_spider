# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import task
from news.models import News
import urllib,urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@task
def spider():
    page_title=urllib2.urlopen('http://news.whu.edu.cn/wdyw.htm').read()
    re_title = r'<a href="info/.*?</a>'
    re_address = r'href=".*?"'
    m_title = re.findall(re_title,page_title)
    type = sys.getfilesystemencoding()   # 关键
    for t in News.objects.all():
        t.delete()
    for i in m_title:
        m_address = re.search(re_address,i).group(0)
        page_content=urllib2.urlopen('http://news.whu.edu.cn/'+m_address[6:-1]).read()
        re_content = r'<span style="font-family.*?</span>'
        m_content = re.findall(re_content, page_content)
        content = "  "
        for k in m_content[0:3]:
            # k.decode("UTF-8").encode(type)
            content+=re.search(r'>.*?<',k).group(0)[1:-1]
        for j in m_content[3:]:
            # j.decode("UTF-8").encode(type)
            content+=re.search(r'>.*?<',j).group(0)[1:-1]
            content+="\n"
            content+="  "
        news = News(title=re.search(r'>.*?<',i).group(0)[1:-1],content=content)
        news.save()