# -*- coding: utf-8 -*-
import urllib
import urllib2
import re


url = 'http://search.51job.com/list/070400,000000,0000,00,9,99,%25E6%2595%25B0%25E5%25AD%25A6%25E8%2580%2581%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('GBK')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

        
content_pattern = re.compile('<span>.*?<a target="_blank".*?title="(.*?)"', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item

content_pattern = re.compile('<span class="t2">.*?>(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item

content_pattern = re.compile('<span class="t3"(.*?)</span>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item

content_pattern = re.compile('<span class="t4"(.*?)</span>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item
